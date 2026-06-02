
from fastapi import FastAPI
from pydantic import BaseModel
from resume_parser import parse_resume
from gap_analyzer import analyze_gaps
from report_generator import generate_report

app = FastAPI()

class ResumeInput(BaseModel):
    resume_text: str

@app.get("/")
def home():
    return {"message": "AI Career Coach is running"}

@app.post("/analyze")
def analyze_resume(input: ResumeInput):
    parsed = parse_resume(input.resume_text)
    gaps = analyze_gaps(parsed["skills_found"])
    report = generate_report(parsed, gaps)
    return {"report": report}