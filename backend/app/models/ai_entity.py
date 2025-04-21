from sqlalchemy import Column, Integer, String
from ..db.database import Base

class AIEntity(Base):
    __tablename__ = 'ai_entities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    job = Column(String)
