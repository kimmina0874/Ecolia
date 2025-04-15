from fastapi import APIRouter
from app.services.ai_agent import ai_agents

router = APIRouter()

@router.get("/api/agents")
def get_agents():
	return [
		{
			"id": a.id, "x": a.x, "y": a.y,
			"age": a.age, "energy": a.energy,
			"sick": a.sick, "task": a.task,
			"village_center": a.village_center
		}
		for a in ai_agents if a.is_alive
	]
