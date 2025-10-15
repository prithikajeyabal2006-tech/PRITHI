from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv('DB_URL', 'mysql+mysqlconnector://root:password@localhost/interview_analysis')

engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class InterviewResult(Base):
    __tablename__ = 'interview_results'
    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String(100))
    transcript = Column(Text)
    sentiment = Column(Float)
    filler_count = Column(Integer)
    keyword_count = Column(Integer)
    final_score = Column(Float)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_result(data: dict):
    db = SessionLocal()
    rec = InterviewResult(
        candidate_name=data.get('candidate_name'),
        transcript=data.get('transcript'),
        sentiment=data.get('sentiment'),
        filler_count=data.get('filler_count'),
        keyword_count=data.get('keyword_count'),
        final_score=data.get('final_score')
    )
    db.add(rec)
    db.commit()
    db.refresh(rec)
    db.close()
    return rec.id
