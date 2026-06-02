# This file reads a resume and finds skills in it

def parse_resume(resume_text: str) -> dict:
    
    # Split the resume into individual words
    words = resume_text.split()
    
    # These are the skills we're looking for
    skills_to_find = ["python", "sql", "machine learning", 
                      "rag", "fastapi", "langchain"]
    
    # Check which skills appear in the resume
    found_skills = [
        skill for skill in skills_to_find 
        if skill.lower() in resume_text.lower()
    ]
    
    # Return what we found
    return {
        "word_count": len(words),
        "skills_found": found_skills,
        "skills_count": len(found_skills)
    }