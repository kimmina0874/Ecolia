import random

TILE_TYPES = ["grass", "tree", "rock", "water", "sand"]
WIDTH = 2000
HEIGHT = 2000

def generate_map(seed=42):
	random.seed(seed)
	return [
		[random.choice(TILE_TYPES) for _ in range(WIDTH)]
		for _ in range(HEIGHT)
	]