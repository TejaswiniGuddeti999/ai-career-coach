# This file compares skills found in resume 
# against skills companies actually want

def analyze_gaps(skills_found: list) -> dict:
    
    # These are skills most AI/ML jobs require
    required_skills = {
        "python": "Core programming language",
        "sql": "Data querying",
        "fastapi": "Backend engineering",
        "langchain": "LLM orchestration",
        "rag": "Retrieval systems",
        "postgresql": "Database management"
    }
    
    # Find which required skills are missing from resume
    missing = {
        skill: desc 
        for skill, desc in required_skills.items() 
        if skill not in skills_found
    }
    
    return {
        "missing_skills": missing,
        "gaps_count": len(missing)
    }
