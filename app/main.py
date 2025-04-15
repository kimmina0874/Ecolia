from fastapi import FastAPI
from app.routes import nation

app = FastAPI()

app.include_router(nation.router)
