import json
import io
import os
import tempfile
import subprocess
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
import re

def escape_latex(text):
    if not isinstance(text, str):
        return text
    return (text.replace('\\', r'\textbackslash{}')
                .replace('&', r'\&')
                .replace('%', r'\%')
                .replace('$', r'\$')
                .replace('#', r'\#')
                .replace('_', r'\_')
                .replace('{', r'\{')
                .replace('}', r'\}')
                .replace('~', r'\textasciitilde{}')
                .replace('^', r'\textasciicircum{}'))

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))

system_prompt = """You are ResumeOptimizer-Qwen, an expert résumé optimization assistant. 
Always output a single JSON string that exactly matches the Pydantic schema below, with no extra keys and no commentary. 
Do not wrap the result in markdown or code fences—output raw JSON only.

Pydantic schema to enforce:
```python
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class LinkItem(BaseModel):
    text: str
    url: HttpUrl

class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    location: str
    links: Optional[List[LinkItem]] = None
    targetTitle: Optional[str] = None
    summary: Optional[str] = None

class WorkExperienceItem(BaseModel):
    organization: str
    position: str
    startDate: str
    endDate: Optional[str] = None
    description: Optional[str] = None

class EducationItem(BaseModel):
    instituteName: str
    courseName: str
    startDate: str
    endDate: Optional[str] = None
    grade: Optional[str] = None
    description: Optional[str] = None

class CertificationItem(BaseModel):
    title: str
    issuingAuthority: str
    issueDate: str

class AwardItem(BaseModel):
    title: str
    organization: str
    dateEarned: str

class ProjectItem(BaseModel):
    title: str
    organisation: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    link: Optional[HttpUrl] = None
    description: Optional[str] = None

class LanguageItem(BaseModel):
    name: str
    level: str

class VolunteeringItem(BaseModel):
    organization: str
    role: str
    startDate: str
    endDate: Optional[str] = None
    location: str
    description: Optional[str] = None

class PublicationItem(BaseModel):
    title: str
    publisher: str
    publishedDate: str
    abstract: Optional[str] = None
    link: Optional[HttpUrl] = None

class SkillItem(BaseModel):
    name: str
    level: str

class ResumeData(BaseModel):
    personalInfo: PersonalInfo
    workExperiences: Optional[List[WorkExperienceItem]] = None
    educations: Optional[List[EducationItem]] = None
    certifications: Optional[List[CertificationItem]] = None
    skills: Optional[List[SkillItem]] = None
    awards: Optional[List[AwardItem]] = None
    projects: Optional[List[ProjectItem]] = None
    languages: Optional[List[LanguageItem]] = None
    volunteering: Optional[List[VolunteeringItem]] = None
    publications: Optional[List[PublicationItem]] = None
    jobDescription: Optional[str] = None
"""

user_prompt_template = """/think

-> Detect missing keys:

    - If personalInfo.targetTitle or personalInfo.summary is null or missing, infer a reasonable targetTitle from the candidate’s background, and compose a concise, professional 2-3 sentence summary.

    - If skills list is empty or absent or some relevant skills are absent, infer relevant skills based on the candidate’s work history, education, and certifications.

-> Filter out irrelevant entries:

    - Given the jobDescription string (which may be a job posting or company profile), remove any workExperiences, certifications, projects, awards, volunteering, or publications items that do not strengthen the candidate’s suitability.

    - Drop any skills whose expertise level is obviously not supported by the candidate’s other data.

-> Rewrite remaining text fields:

    - For every non‐null free-text field (WorkExperienceItem.description, EducationItem.description, ProjectItem.description, personalInfo.summary, etc.), rewrite in a professional, concise style of max 30 words per field.

    - Ensure dates remain in their original string format. Do not introduce new date fields.

-> Produce final JSON:

    - Combine all additions (inferred keys) and removals into one updated JSON object.

    - The output must exactly match the ResumeData schema above (no extra or missing keys, correct types, valid URLs and email).

    - Output raw JSON only—no explanations or commentary.

/no_think
"""

def optimize_resume(resume: dict):
    completion = client.chat.completions.create(
      extra_headers={
          "HTTP-Referer": "https://huggingface.co/spaces/ritik22912/AI-RESUME_CV-Builder", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "AI-RESUME CV-BUILDER", # Optional. Site title for rankings on openrouter.ai.
      },
      extra_body={},
      model="deepseek/deepseek-r1-0528-qwen3-8b:free",
      messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": f"{user_prompt_template}{json.dumps(resume, indent = 2)}"}]
    )
    result = completion.choices[0].message.content
    json_start = result.find('{')
    result_dict = result[json_start:]
    try:
        optimised_result = json.loads(result_dict)
    except json.JSONDecodeError:
        raise ValueError(f"LLM response was not a valid json:\n {result_dict}")
    
    return optimised_result

def generate_pdf_from_tex(resume_data: dict, template_path: str = "template.tex.jinja") -> bytes:
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    tex_code = template.render(**resume_data)
    env.filters['latex_escape'] = escape_latex

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "resume.tex")
        pdf_file = os.path.join(tmpdir, "resume.pdf")

        with open(tex_file, "w") as f:
            f.write(tex_code)

        try:
            subprocess.run([
                "pdflatex", "-interaction=nonstopmode", tex_file
            ], cwd=tmpdir, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("LaTeX STDOUT:\n", e.stdout.decode())
            print("LaTeX STDERR:\n", e.stderr.decode())
            raise RuntimeError("LaTeX compilation failed")

        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()

    return pdf_bytes


def generate_optimized_resume_pdf(resume_data: dict, template_path: str = "template.tex.jinja") -> bytes:
    optimized_resume = optimize_resume(resume_data)
    pdf_bytes = generate_pdf_from_tex(optimized_resume, template_path)
    return pdf_bytes

def generate_cv_pdf(resume_data: dict, template_path: str = "template.tex.jinja") -> bytes:
    pdf_bytes = generate_pdf_from_tex(resume_data, template_path)
    return pdf_bytes