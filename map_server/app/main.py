from fastapi import FastAPI
from app.routes import map

app = FastAPI()
app.include_router(map.router)
