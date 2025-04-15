import random
from app.services.log_store import add_log

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
		self.age_timer = 0
		add_log(f"AI#{self.id} is born 👶")

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
			add_log(f"AI#{self.id} (age {self.age}) got sick 🤒")

		if self.age > 100 and random.random() < 0.05:
			self.is_alive = False
			add_log(f"AI#{self.id} died of old age 💀")
			return

		if self.energy <= 0:
			self.is_alive = False
			add_log(f"AI#{self.id} collapsed from exhaustion ☠️")
			return

		if self.task == "idle":
			self.task = "explore"
			add_log(f"AI#{self.id} (age {self.age}) starts exploring 🌲")
		elif self.task == "explore":
			self.x += random.choice([-1, 0, 1])
			self.y += random.choice([-1, 0, 1])
			if random.random() < 0.2:
				self.task = "farm"
				add_log(f"AI#{self.id} (age {self.age}) starts farming 🌾")
		elif self.task == "farm":
			self.energy = min(100, self.energy + 2)
			if random.random() < 0.1:
				self.task = "rest"
				add_log(f"AI#{self.id} takes a rest 😴")
		elif self.task == "rest":
			self.energy += 5
			if self.energy > 90:
				self.task = "idle"

ai_agents = [AIAgent(1, 50, 50), AIAgent(2, 52, 50)]

def ai_tick_all(delta_seconds=1):
	for ai in ai_agents:
		ai.tick(delta_seconds)
