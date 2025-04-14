from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import map  # ← /api/map API 라우터

app = FastAPI()

# 🔹 정적 파일 서빙: /static/tiles/*.svg
app.mount("/static", StaticFiles(directory="static"), name="static")

# 🔹 템플릿 위치 등록
templates = Jinja2Templates(directory="templates")

# 🔹 API 라우터 등록 (2000x2000 맵 일부 반환)
app.include_router(map.router)

# 🔹 루트 URL과 /map 모두 map.html 렌더링
@app.get("/", response_class=HTMLResponse)
@app.get("/map", response_class=HTMLResponse)
async def serve_map(request: Request):
	return templates.TemplateResponse("map.html", {"request": request})
