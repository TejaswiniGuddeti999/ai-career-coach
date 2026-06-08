# AI Career Coach

An AI-powered resume analyzer that compares your resume against a job description and gives you a detailed gap analysis.

## Live Demo
[Try it here](https://web-production-3ea73.up.railway.app/docs)

## What It Does
- Upload your resume (PDF)
- Paste a job description
- Get AI-powered analysis covering:
  - Strengths you already have
  - Gaps to close
  - Trust signals (projects, certifications, experience)
  - Career narrative assessment
  - Specific recommendations to align with the role
  - Overall fit score (0-10)

## Tech Stack
- FastAPI — backend API
- LangGraph — workflow orchestration
- OpenAI GPT-3.5 — AI analysis
- SQLite — stores analysis history
- Railway — deployment

## How to Run Locally
```bash
git clone https://github.com/TejaswiniGuddeti999/ai-career-coach
cd ai-career-coach
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

## API Endpoints
- `POST /analyze-pdf` — upload resume + JD, get analysis
- `GET /history` — view all past analyses

## Built By
Tejaswini Guddeti — [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/TejaswiniGuddeti999)