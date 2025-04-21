from fastapi import APIRouter
from ..models.resource import Resource
from ..db.database import SessionLocal

router = APIRouter()

@router.get("/resources")
def get_resources():
    db = SessionLocal()
    resources = db.query(Resource).all()
    return resources
