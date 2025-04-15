from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes import api

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(api.router)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})
