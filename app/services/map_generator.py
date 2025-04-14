from noise import pnoise2

TILE_TYPES = ["ocean", "beach", "river", "desert", "grass", "forest", "mountain"]
WIDTH = 2000
HEIGHT = 2000

def generate_map(scale=100.0, octaves=6):
	map_data = []
	for y in range(HEIGHT):
		row = []
		for x in range(WIDTH):
			elevation = pnoise2(x / scale, y / scale, octaves=octaves)

			if elevation < -0.3:
				tile = "ocean"
			elif elevation < -0.1:
				tile = "beach"
			elif elevation < 0.05:
				tile = "river"
			elif elevation < 0.2:
				tile = "desert"
			elif elevation < 0.4:
				tile = "grass"
			elif elevation < 0.65:
				tile = "forest"
			else:
				tile = "mountain"

			row.append(tile)
		map_data.append(row)
	return map_data