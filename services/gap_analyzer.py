import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_gaps(resume_text: str, job_description: str) -> dict:
    """
    AI analyzes resume against JD holistically
    Evaluates: competence, trust signals, consistency, career narrative
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """You are an expert recruiter evaluating a candidate.

Analyze this resume against the job description on these dimensions:

1. COMPETENCE: Can they finish what they start? (Look for: project completion, scope of work, impact metrics)
2. TRUST SIGNALS: Evidence of real work (GitHub links, LinkedIn, verified certificates, published work)
3. CONSISTENCY: How committed are they? (Career progression, skill depth, continuous learning)
4. CAREER NARRATIVE: Is their journey coherent? (Any gaps? Growth patterns? Industry switches?)
5. JOB MATCH: How aligned are they to this specific role?

Return ONLY valid JSON (no markdown):
{
    "strengths": ["top 3 strongest aspects"],
    "gaps": ["what they're missing for this role"],
    "trust_signals": ["evidence of real work and credibility"],
    "competence_assessment": "1-2 sentences on execution capability",
    "career_narrative": "1-2 sentences on career progression and any gaps",
    "specific_recommendations": ["3-5 concrete actions to better align with JD"],
    "overall_fit_score": "0-10 with brief reasoning"
}"""
            },
            {
                "role": "user",
                "content": f"RESUME:\n{resume_text}\n\nJOB DESCRIPTION:\n{job_description}"
            }
        ]
    )
    
    return response.choices[0].message.content