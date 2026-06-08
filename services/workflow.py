from langgraph.graph import StateGraph, END
from typing import TypedDict
from services.gap_analyzer import analyze_gaps

class ResumeState(TypedDict):
    resume_text : str
    job_description: str
    analysis: dict


#each function is one node in workflow

def analyze_node(state: ResumeState) -> ResumeState:
    state['analysis'] = analyze_gaps(state['resume_text'], state['job_description'])
    return state

def build_workflow():
    workflow = StateGraph(ResumeState)
    workflow.add_node("analyze", analyze_node)
    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", END)
    return workflow.compile()