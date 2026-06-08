from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Creates a local SQLite database file
engine = create_engine("sqlite:///career_coach.db")
Base = declarative_base()


#defines what one analysis record look like
class Analysis(Base):
    __tablename__ = "analyses"
    
    id = Column(Integer, primary_key=True)
    # When was this analysis done
    created_at = Column(DateTime, default=datetime.utcnow)
    # Store the inputs
    resume_text = Column(Text)
    job_description = Column(Text)
    # Store the result
    result = Column(Text)

#create a table if it doesnt exist
Base.metadata.create_all(engine)

#funtion to save one analysis
def save_analysis(resume_text: str, job_description: str, result:str):
    Session = sessionmaker(bind=engine)
    session = Session()

    analysis = Analysis(
        resume_text=resume_text,
        job_description=job_description,
        result=result
    )

    session.add(analysis)
    session.commit()
    session.close()

#function to get all past analyses
def get_all_analyses():
    Session = sessionmaker(bind= engine)
    session = Session()
    analyses = session.query(Analysis).all()
    session.close()
    return analyses