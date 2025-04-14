from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import map

app = FastAPI()

# 정적 파일 (타일 이미지) 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML 템플릿 (map.html) 위치 설정
templates = Jinja2Templates(directory="templates")

# API 라우터 연결
app.include_router(map.router)

# ✅ 루트 URL로 접속하면 map.html 렌더링
@app.get("/", response_class=HTMLResponse)
@app.get("/map", response_class=HTMLResponse)
def serve_map(request: Request):
	return templates.TemplateResponse("map.html", {"request": request})
