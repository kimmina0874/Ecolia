# app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import map  # 라우터는 map.py에서 처리

app = FastAPI()

# 정적 파일 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

# API 라우터 등록
app.include_router(map.router)

# 기본 페이지: map.html 렌더링
@app.get("/", response_class=HTMLResponse)
@app.get("/map", response_class=HTMLResponse)
async def serve_map(request: Request):
	return templates.TemplateResponse("map.html", {"request": request})
