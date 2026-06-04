from fastapi import APIRouter, UploadFile, File, Form
from services.resume_parser import parse_resume
from services.gap_analyzer import analyze_gaps, get_ai_feedback
from services.report_generator import generate_report
from pdf_reader import extract_text_from_pdf

#APIRouter is like a mini FastAPI which groups related endpoints
router = APIRouter()

@router.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...),
                job_description: str = Form(...)
):
    contents = await file.read()
    resume_text = extract_text_from_pdf(contents)
    parsed = parse_resume(resume_text)
    gaps = analyze_gaps(parsed["skills_found"])
    report = generate_report(parsed, gaps)
    feedback = get_ai_feedback(resume_text, job_description)

    return {"report" : report,
        "ai_feedback" :feedback}