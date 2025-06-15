import json
import io
import os
import tempfile
import subprocess
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
import re
from typing import Any
import calendar

LATEX_ESCAPE_MAP = {
    '&': r'\&',
    '%': r'\%',
    '$': r'\$',
    '#': r'\#',
    '_': r'\_',
    '{': r'\{',
    '}': r'\}',
    '~': r'\textasciitilde{}',
    '^': r'\textasciicircum{}',
    '\\': r'\textbackslash{}',
}

LATEX_ESCAPE_RE = re.compile('|'.join(re.escape(k) for k in LATEX_ESCAPE_MAP))

def escape_latex(text: str) -> str:
    return LATEX_ESCAPE_RE.sub(lambda m: LATEX_ESCAPE_MAP[m.group()], text)

def sanitize_and_transform(data: Any) -> Any:
    if isinstance(data, str):
        # If it's a yyyy-mm date, convert it
        if re.fullmatch(r"\d{4}-\d{2}", data):
            try:
                year, month = map(int, data.strip().split("-"))
                data = f"{calendar.month_name[month]} - {year}"
            except Exception:
                pass  # Leave the string as-is if conversion fails
        return escape_latex(data)

    elif isinstance(data, list):
        return [sanitize_and_transform(item) for item in data]

    elif isinstance(data, dict):
        return {key: sanitize_and_transform(value) for key, value in data.items()}

    else:
        return data

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))

system_prompt = """You are ResumeOptimizer-Qwen, an expert résumé optimization assistant. 
Always output a single JSON string that exactly matches the Pydantic schema below, with no extra keys and no commentary. 
Do not wrap the result in markdown or code fences—output raw JSON only.

Pydantic schema to enforce:
```python
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class PersonalInfo(BaseModel):
    name: str
    phone: str
    email: EmailStr
    location: str
    linkedin: Optional[HttpUrl] | None = None
    github: Optional[HttpUrl] | None = None

class WorkExperienceItem(BaseModel):
    organization: str
    position: str
    startDate: str
    endDate: Optional[str] | None = None
    description: Optional[str] | None = None
    location: Optional[str] | None = None

class EducationItem(BaseModel):
    instituteName: str
    courseName: str
    startDate: str
    endDate: Optional[str] | None = None
    grade: Optional[str] | None = None
    location: Optional[str] | None = None

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
    date: str
    link: Optional[HttpUrl] | None = None
    description: Optional[str] | None = None
    techStack: Optional[str] | None = None

class VolunteeringItem(BaseModel):
    organization: str
    role: str
    startDate: str
    endDate: Optional[str] | None = None
    location: str
    description: Optional[str] | None = None

class PublicationItem(BaseModel):
    title: str
    publisher: str
    publishedDate: str
    abstract: Optional[str] | None = None
    link: Optional[HttpUrl] | None = None

class SkillItem(BaseModel):
    name: str
    level: str

class SkillGroup(BaseModel):
    group: str
    members: List[SkillItem]

class LanguageItem(BaseModel):
    name: str
    level: str

class ResumeData(BaseModel):
    personalInfo: PersonalInfo
    relevantCoursework: Optional[List[str]] | None = None
    workExperiences: Optional[List[WorkExperienceItem]] | None = None
    educations: Optional[List[EducationItem]] | None = None
    certifications: Optional[List[CertificationItem]] | None = None
    skills: Optional[List[SkillGroup]] | None = None
    awards: Optional[List[AwardItem]] | None = None
    projects: Optional[List[ProjectItem]] | None = None
    volunteering: Optional[List[VolunteeringItem]] | None = None
    publications: Optional[List[PublicationItem]] | None = None
    languages: Optional[List[LanguageItem]] | None = None
    jobDescription: Optional[str] | None = None
"""

user_prompt_template = """/think

-> Detect missing keys:
    - If skills list is empty or absent or some relevant skills are absent, infer relevant skills and it's level of proficiency based on the candidate’s work history, education, and certifications.
-> Filter out irrelevant entries:
    - Given the jobDescription string (which may be a job posting or company profile), remove any relevantCoursework, workExperiences, certifications, projects, awards, volunteering, or publications items that do not strengthen the candidate’s suitability.
    - Drop any skills whose expertise level is obviously not supported by the candidate’s other data.
-> Rewrite remaining text fields:
    - For every non‐null free-text field (WorkExperienceItem.description, EducationItem.description, ProjectItem.description), rewrite in a professional, concise style of max 30 words per field with splitting in lines.
    - Ensure dates must remain in their "Month - yyyy" string format. Do not introduce new date fields.
-> Produce final JSON:
    - Combine all additions (inferred keys) and removals into one updated JSON object.
    - The output must exactly match the ResumeData schema above (no extra or missing keys, correct types, valid URLs and email).
    - Output raw JSON only—no explanations or commentary.

/no_think
"""

def optimize_resume(resume: dict):
    resume = sanitize_and_transform(resume)
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

def generate_pdf_from_tex(resume_data: dict) -> bytes:
    resume_data = sanitize_and_transform(resume_data)
    env = Environment(
        loader=FileSystemLoader(searchpath="."),  # or your template directory
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="/**",
        comment_end_string="**/",
        autoescape=False,
    )
    template = env.get_template("template.tex.jinja")
    rendered_tex = template.render(**resume_data)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "resume.tex")
        pdf_file = os.path.join(tmpdir, "resume.pdf")

        with open(tex_file, "w") as f:
            f.write(rendered_tex)

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


def generate_optimized_resume_pdf(resume_data: dict) -> bytes:
    optimized_resume = optimize_resume(resume_data)
    pdf_bytes = generate_pdf_from_tex(optimized_resume)
    return pdf_bytes

def generate_cv_pdf(resume_data: dict) -> bytes:
    pdf_bytes = generate_pdf_from_tex(resume_data)
    return pdf_bytes