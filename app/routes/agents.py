from fastapi import APIRouter
from app.services.ai_agent import ai_agents

router = APIRouter()

@router.get("/api/agents")
def get_agents():
	return {"agents": [a.get_status() for a in ai_agents]}
