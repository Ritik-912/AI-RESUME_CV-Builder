from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import ValidationError
from data_model import ResumeData
from generate_resume import generate_cv_pdf, generate_optimized_resume_pdf
# from cv_parser import parse_cv
import json
import io
import logging

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume Generator API", version="1.0.0")

# Add this CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your Vite frontend origin
    allow_credentials=True,
    allow_methods=["POST"],  # allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # allow all headers
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_empty(data):
    if isinstance(data, dict):
        return {k: clean_empty(v) for k, v in data.items() if v not in ("", None, [], {})}
    elif isinstance(data, list):
        return [clean_empty(i) for i in data if i not in ("", None, [], {})]
    return data


@app.post("/generate-cv", response_class=StreamingResponse)
def generate_cv(data: ResumeData):
    """
    Generate a general CV PDF from structured resume data.
    """
    try:
        from fastapi.encoders import jsonable_encoder

        raw_data = jsonable_encoder(data)
        cleaned_data = clean_empty(raw_data)

        logger.log(msg=f"Cleaned resume data: {json.dumps(cleaned_data, indent=2)}", level=logging.INFO)
        pdf_bytes = generate_cv_pdf(cleaned_data)
        pdf_stream = io.BytesIO(pdf_bytes)
        return StreamingResponse(pdf_stream, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=CV.pdf"})
    except Exception as e:
        logger.error(f"Error generating CV: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate CV PDF")

@app.post("/generate-resume", response_class=StreamingResponse)
async def generate_resume(
    data: str = Form(...)
):
    """
    Generate an optimized resume tailored to a job description.
    """
    try:
        parsed_data = json.loads(data)
        pdf_bytes = generate_optimized_resume_pdf(parsed_data)
        pdf_stream = io.BytesIO(pdf_bytes)
        return StreamingResponse(pdf_stream, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=Resume.pdf"})
    except json.JSONDecodeError as e:
        logger.warning(f"Invalid JSON input: {e}")
        raise HTTPException(status_code=400, detail="Invalid resume data format")
    except Exception as e:
        logger.error(f"Error generating resume: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate optimized resume")

@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    """
    Upload a CV (PDF or DOCX) and parse it into structured resume data.
    """
    try:
        content = await file.read()
        parsed_data = {'name': "Hello!"}# parse_cv(content)
        return JSONResponse(content=parsed_data)
    except Exception as e:
        logger.error(f"Error parsing uploaded CV: {e}")
        raise HTTPException(status_code=500, detail="Failed to parse the uploaded CV")