from fastapi import APIRouter
from app.services.ai_agent import ai_agents

router = APIRouter()

@router.get("/api/agents")
def get_agents():
	return [
		{"id": a.id, "x": a.x, "y": a.y, "age": a.age, "energy": a.energy, "task": a.task}
		for a in ai_agents if a.is_alive
	]
