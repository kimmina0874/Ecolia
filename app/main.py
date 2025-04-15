from fastapi import APIRouter, Query
from app.services.map_generator import generate_map

router = APIRouter()
full_map = generate_map()

@router.get("/api/map")
def get_map(
	x: int = Query(0, ge=0, le=1999),
	y: int = Query(0, ge=0, le=1999),
	size: int = Query(20, ge=1, le=100)
):
	x_end = min(x + size, len(full_map[0]))
	y_end = min(y + size, len(full_map))
	section = [row[x:x_end] for row in full_map[y:y_end]]

	return {
		"origin": [x, y],
		"size": size,
		"tiles": section
	}

# ✅ 미니맵용 API 추가
@router.get("/api/minimap")
def get_minimap():
	color_map = {
		"ocean": "#2980b9",
		"beach": "#f9ca24",
		"river": "#74b9ff",
		"desert": "#f6e58d",
		"grass": "#6ab04c",
		"forest": "#27ae60",
		"mountain": "#7f8c8d"
	}
	# 전체 2000x2000 중 100x100 축소 반환
	minimap = [[color_map[tile] for tile in row[::20]] for row in full_map[::20]]
	return {"minimap": minimap}
