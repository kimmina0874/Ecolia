import random

def generate_map(width=2000, height=2000):
	tiles = ["grass", "forest", "desert", "sand", "rock", "water"]
	return [[random.choice(tiles) for _ in range(width)] for _ in range(height)]

full_map = generate_map()
