import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_gaps(resume_text: str, job_description: str) -> dict:
    """
    AI analyzes resume against a JD holistically
    Covers: skills, expereince , certifications, courses, projects, education
    """

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
            "role": "system",
            "content": """You are an expert recruiter and career coach doing a thorough resume evaluation.

            Analyze the resume against the job description carefully. Follow this exact process:

            STEP 1 - PARSE RESUME SECTIONS:
            Extract and evaluate each section present:
            - Contact details and professional links (LinkedIn, GitHub, HuggingFace, portfolio)
            - Professional summary
            - Work experience (extract each role with company, title, start date, end date)
            - Projects (personal and professional, note any GitHub/demo links)
            - Skills
            - Education (institution, degree, year)
            - Certifications and courses (note if links/certificates are attached)
            - Publications or research

            STEP 2 - CALCULATE CAREER TIMELINE:
            - List all roles in chronological order with dates
            - Calculate duration of each role
            - Identify any gaps between roles (gap = more than 2 months between end of one role and start of next)
            - Calculate total years of experience
            - Note: internship comes BEFORE full time role in timeline

            STEP 3 - EVALUATE TRUST SIGNALS:
            - Are GitHub/project links present? 
            - Are certifications verifiable?
            - Do project descriptions show real outcomes or just descriptions?
            - Is experience backed by recognizable companies or institutions?

            STEP 4 - ASSESS COMPETENCE:
            - Did they complete projects end to end?
            - Do they show measurable impact (numbers, metrics, improvements)?
            - Is skill depth evident or just surface level?

            STEP 5 - EVALUATE JOB FIT:
            - Which requirements from JD are clearly met?
            - Which are partially met?
            - Which are missing entirely?

            Return ONLY valid JSON (no markdown, no backticks):
            {
                "sections_found": ["list of resume sections detected"],
                "professional_links": ["any URLs or profile links found"],
                "career_timeline": [
                    {"role": "", "company": "", "start": "", "end": "", "duration": ""}
                ],
                "career_gaps": [
                    {"from": "", "to": "", "duration": "", "reason_if_mentioned": ""}
                ],
                "total_experience_years": "",
                "trust_signals": ["evidence of real credible work"],
                "competence_assessment": "2-3 sentences on execution and impact",
                "strengths": ["top strengths relevant to this role"],
                "gaps": ["what is missing for this specific role"],
                "recommendations": ["3-5 specific actionable steps to close gaps"],
                "overall_fit_score": "X/10 with one line reasoning"
            }"""
                },
                {"role" : "user",
                "content": f"RESUME:\n{resume_text}\n\JOB DESCRIPTION:\n{job_description}"
                }
    ])
    return response.choices[0].message.content 