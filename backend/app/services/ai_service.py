from ..models.ai_entity import AIEntity
from ..db.database import SessionLocal

def run_simulation():
    db = SessionLocal()
    # 예시: AI들의 행동을 업데이트하는 로직
    ai_entities = db.query(AIEntity).all()
    for ai in ai_entities:
        ai.age += 1  # AI의 나이를 증가시킴
    db.commit()
