from fastapi import APIRouter, HTTPException
from ..models.ai_entity import AIEntity
from ..db.database import SessionLocal

router = APIRouter()

@router.get("/ai/{ai_id}")
def get_ai(ai_id: int):
    db = SessionLocal()
    ai = db.query(AIEntity).filter(AIEntity.id == ai_id).first()
    if ai is None:
        raise HTTPException(status_code=404, detail="AI not found")
    return ai
