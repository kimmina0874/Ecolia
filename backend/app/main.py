from fastapi import FastAPI
from .api import ai, resources, simulation
from .db.database import engine
from .models import Base

# FastAPI 앱 생성
app = FastAPI()

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# API 라우팅
app.include_router(ai.router)
app.include_router(resources.router)
app.include_router(simulation.router)

@app.get("/")
def read_root():
    return {"message": "AI Civilization Simulation API"}
