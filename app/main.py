from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import map

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(map.router)

@app.get("/", response_class=HTMLResponse)
@app.get("/map", response_class=HTMLResponse)
def serve_map(request: Request):
	return templates.TemplateResponse("map.html", {"request": request})