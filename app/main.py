from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import map, ai
from app.services.ai_agent import ai_tick_all
import asyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(map.router)
app.include_router(ai.router)

@app.get("/", response_class=HTMLResponse)
@app.get("/map", response_class=HTMLResponse)
async def serve_map(request: Request):
	return templates.TemplateResponse("map.html", {"request": request})

@app.on_event("startup")
async def start_ai_loop():
	async def run_loop():
		while True:
			ai_tick_all(delta_seconds=1)
			await asyncio.sleep(1)
	asyncio.create_task(run_loop())
