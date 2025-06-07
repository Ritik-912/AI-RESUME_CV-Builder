from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from pydantic import ValidationError
from data_model import ResumeData
from generate_resume import generate_cv_pdf, generate_optimized_resume_pdf
import io
import json
import logging
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Resume Generator API", version="1.0.0")

# Serve static files (Vue build)
app.mount("/assets", StaticFiles(directory="./assets", html=True), name="frontend")

# Add this CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # allow all headers
)

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@app.get("/")
async def root():
    return FileResponse("./index.html")

# Optional: Fallback to index.html for Vue routing
@app.get("/{full_path:path}")
async def vue_router(full_path: str):
    return FileResponse("./index.html")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/generate-cv", response_class=StreamingResponse)
def generate_cv(data: ResumeData):
    """ Generate a general CV PDF from structured resume data."""
    try:
        data = jsonable_encoder(data)
        pdf_bytes = generate_cv_pdf(data)
        pdf_stream = io.BytesIO(pdf_bytes)
        return StreamingResponse(pdf_stream, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=CV.pdf"})
    except Exception as e:
        logger.error(f"Error generating CV: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate CV PDF")

@app.post("/generate-resume", response_class=StreamingResponse)
async def generate_resume(data: ResumeData):
    """ Generate an optimized resume tailored to a job description."""
    try:
        data = jsonable_encoder(data)
        pdf_bytes = generate_optimized_resume_pdf(data)
        pdf_stream = io.BytesIO(pdf_bytes)
        return StreamingResponse(pdf_stream, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=Resume.pdf"})
    except json.JSONDecodeError as e:
        logger.warning(f"Invalid JSON input: {e}")
        raise HTTPException(status_code=400, detail="Invalid resume data format")
    except Exception as e:
        logger.error(f"Error generating resume: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate optimized resume")