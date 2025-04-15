from fastapi import APIRouter
from app.services.log_store import get_logs

router = APIRouter()

@router.get("/api/logs")
def fetch_logs():
	return {"logs": get_logs()}
