from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routes import log, ai
from app.services.ai_agent import ai_tick_all
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(log.router)
app.include_router(ai.router)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
	return templates.TemplateResponse("logs.html", {"request": request})

@app.on_event("startup")
async def start_loop():
	async def run_loop():
		while True:
			ai_tick_all(delta_seconds=1)
			await asyncio.sleep(1)
	asyncio.create_task(run_loop())
