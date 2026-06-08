from fastapi import APIRouter, UploadFile, File, Form
from pdf_reader import extract_text_from_pdf
from services.workflow import build_workflow
from services.database import save_analysis, get_all_analyses
import json

router = APIRouter()

@router.post("/analyze-pdf")
async def analyze_pdf(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read and convert PDF
    contents = await file.read()
    resume_text = extract_text_from_pdf(contents)
    
    # Build and run the workflow
    workflow = build_workflow()
    result = workflow.invoke({
        "resume_text": resume_text,
        "job_description": job_description,
        "analysis":{}
    })
    # Save to database
    save_analysis(
        resume_text=resume_text,
        job_description=job_description,
        result=json.dumps(result["analysis"])
    )
    
    return result["analysis"]
    
# New endpoint to see all past analyses
@router.get("/history")
def get_history():
    analyses = get_all_analyses()
    return [
        {
            "id": a.id,
            "created_at": a.created_at,
            "result": a.result
        }
        for a in analyses
    ] 