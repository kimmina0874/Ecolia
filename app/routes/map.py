from fastapi import APIRouter, Query
from app.services.map_generator import generate_map, full_map

router = APIRouter()

@router.get("/api/map")
def get_map(x: int = Query(0), y: int = Query(0), size: int = Query(10)):
	tiles = [row[x:x+size] for row in full_map[y:y+size]]
	return {"tiles": tiles}

@router.get("/api/minimap")
def get_minimap():
	color_map = {
		"water": "#3498db", "forest": "#2ecc71", "desert": "#f1c40f",
		"rock": "#95a5a6", "sand": "#f39c12", "grass": "#27ae60"
	}
	return {
		"minimap": [[color_map.get(tile, "#bdc3c7") for tile in row[::20]] for row in full_map[::20]]
	}
