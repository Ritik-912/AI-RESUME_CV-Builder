import json
import io
import os
import tempfile
import subprocess
from jinja2 import Environment, FileSystemLoader
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

PRE_PROMPT_TEMPLATE = """You are a resume optimization assistant.

Your task:
Given a job description and raw resume data in JSON format, return an optimized, professional, and relevant resume JSON.

Instructions:
- Select and retain only the most relevant experiences, skills, and achievements that best match the job description or company profile.
- Remove irrelevant or redundant entries (such as unrelated jobs, skills, or projects).
- Rewrite all retained content to sound polished, concise, and professional — do NOT exaggerate or fabricate information.
- Optimize the 'summary' field: even if it's empty or missing, generate a strong, professional summary aligned with the job or company.
- Limit the output to the most compelling content that would fit a 1-page resume (tight, focused, and high-impact).
- Maintain the original JSON structure and key names, but reduce to only the most relevant and optimized fields.
- Output ONLY the final, minimized JSON string — no extra explanations or comments.

Job Description & Resume Data:
"""

def optimize_resume(resume_data: dict, model_name: str = "mistralai/Mistral-7B-Instruct-v0.2") -> dict:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto")
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    prompt = f"{PRE_PROMPT_TEMPLATE}\n{json.dumps(resume_data)}"

    result = generator(prompt, max_new_tokens=2048, do_sample=True, temperature=0.7)[0]['generated_text']

    json_start = result.find('{')
    optimized_str = result[json_start:]
    try:
        optimized_data = json.loads(optimized_str)
    except json.JSONDecodeError:
        raise ValueError("LLM output was not valid JSON")

    return optimized_data


def generate_pdf_from_tex(resume_data: dict, template_path: str = "template.tex.jinja") -> bytes:
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    tex_code = template.render(**resume_data)

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = os.path.join(tmpdir, "resume.tex")
        pdf_file = os.path.join(tmpdir, "resume.pdf")

        with open(tex_file, "w") as f:
            f.write(tex_code)

        try:
            subprocess.run([
                "pdflatex", "-interaction=nonstopmode", tex_file
            ], cwd=tmpdir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
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