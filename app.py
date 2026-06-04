
from fastapi import FastAPI, UploadFile, File, Form
from pdf_reader import extract_text_from_pdf
from resume_parser import parse_resume
from gap_analyzer import analyze_gaps, get_ai_feedback
from report_generator import generate_report

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Welcome to the Resume Gap Analyzer API!'}

#accepts pdf file upload
@app.post("//analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...),
                job_description: str = Form(...)
):
    contents = await file.read()

    resume_text = extract_text_from_pdf(contents)

    # Run through our pipeline
    parsed = parse_resume(resume_text)
    gaps = analyze_gaps(parsed["skills_found"])
    report = generate_report(parsed, gaps)
    feedback = get_ai_feedback(resume_text, job_description)

    return {"report": report,
            "ai_feedback": feedback}