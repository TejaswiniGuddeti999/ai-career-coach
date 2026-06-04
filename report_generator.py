
# This file takes the parsed resume and gaps
# and creates a final readable report

def generate_report(parsed: dict, gaps: dict) -> str:
    
    report = f"""
    CAREER GAP REPORT
    -----------------
    Skills found in your resume: {parsed['skills_count']}
    Skills identified: {', '.join(parsed['skills_found'])}
    
    Gaps to close: {gaps['gaps_count']}
    Missing skills:
    """
    
    for skill, desc in gaps['missing_skills'].items():
        report += f"\n    - {skill}: {desc}"
    
    return report