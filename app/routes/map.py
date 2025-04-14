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