import random

class AIAgent:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y
		self.age = 0
		self.energy = 100
		self.is_alive = True
		self.sick = False
		self.task = "idle"
		self.village_center = None
		self.age_timer = 0

	def tick(self, delta_seconds=1):
		if not self.is_alive:
			return

		self.age_timer += delta_seconds
		if self.age_timer >= 3600:
			self.age += 1
			self.age_timer = 0

		self.energy -= 1 if not self.sick else 2

		if not self.sick and random.random() < 0.01:
			self.sick = True
		if self.age > 100 and random.random() < 0.05:
			self.is_alive = False
		if self.energy <= 0:
			self.is_alive = False

		if self.task == "idle":
			if not self.village_center and random.random() < 0.1:
				self.task = "build_village"
			else:
				self.task = "explore"
		elif self.task == "explore":
			self.x += random.choice([-1, 0, 1])
			self.y += random.choice([-1, 0, 1])
			if random.random() < 0.2:
				self.task = "idle"
		elif self.task == "build_village":
			self.village_center = (self.x, self.y)
			self.task = "farm"
		elif self.task == "farm":
			self.energy = min(100, self.energy + 3)
			if random.random() < 0.05:
				self.task = "idle"

ai_agents = [
	AIAgent(id=1, x=100, y=100),
	AIAgent(id=2, x=120, y=100)
]

def ai_tick_all(delta_seconds=1):
	for ai in ai_agents:
		ai.tick(delta_seconds)
	alive = [a for a in ai_agents if a.is_alive]
	for i, a1 in enumerate(alive):
		for a2 in alive[i+1:]:
			if abs(a1.x - a2.x) < 5 and abs(a1.y - a2.y) < 5:
				new_ai = AIAgent(id=len(ai_agents) + 1, x=a1.x, y=a1.y)
				ai_agents.append(new_ai)
				break
