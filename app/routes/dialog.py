from fastapi import APIRouter
from app.services.dialog_logger import get_dialogs

router = APIRouter()

@router.get("/api/dialogs")
def fetch_dialogs(level: str = "all"):
	return {"dialogs": get_dialogs(level)}
