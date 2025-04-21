from fastapi import APIRouter
from ..services.ai_service import run_simulation

router = APIRouter()

@router.post("/simulate")
def simulate():
    run_simulation()
    return {"message": "Simulation running"}
