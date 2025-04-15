from fastapi import APIRouter
from app.services.simulation import get_logs, get_agents, get_nation_structure

router = APIRouter()

@router.get("/api/logs")
def logs():
	return {"logs": get_logs()}

@router.get("/api/agents")
def agents():
	return {"agents": get_agents()}

@router.get("/api/nation")
def nation():
	return get_nation_structure()
