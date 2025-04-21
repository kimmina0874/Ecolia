from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Integer)
    ai_entity_id = Column(Integer, ForeignKey('ai_entities.id'))
    owner = relationship("AIEntity")
