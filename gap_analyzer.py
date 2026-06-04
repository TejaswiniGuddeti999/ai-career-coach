import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_gaps(skills_found: list) -> dict:
    required_skills = {
        "python": "Core programming language",
        "sql": "Data querying",
        "fastapi": "Backend engineering",
        "langchain": "LLM orchestration",
        "rag": "Retrieval systems",
        "postgresql": "Database management"
    }
    
    missing = {
        skill: desc 
        for skill, desc in required_skills.items() 
        if skill not in skills_found
    }
    
    return {
        "missing_skills": missing,
        "gaps_count": len(missing)
    }

def get_ai_feedback(resume_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a career coach. Analyze this resume and give 3 specific improvements."},
            {"role": "user", "content": resume_text}
        ]
    )
    return response.choices[0].message.content