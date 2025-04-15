import random
from app.services.log_store import add_log
from app.services.dialog_logger import add_dialog

class AIAgent:
	def __init__(self, id, name, gender, x, y):
		self.id = id
		self.name = name
		self.gender = gender
		self.x = x
		self.y = y
		self.age = 0
		self.hunger = 100
		self.sleepiness = 0
		self.belonging = 50
		self.energy = 100
		self.task = "idle"
		self.is_alive = True
		add_log(f"👶 {self.name}({self.gender})가 태어났습니다.")
		add_dialog("village", f"{self.name}이 마을에 합류했습니다.")

	def tick(self, delta_seconds):
		if not self.is_alive:
			return
		self.age += 1
		self.hunger -= 5
		self.sleepiness += 3
		self.belonging -= 2

		if self.hunger < 30:
			self.task = "eat"
			add_log(f"{self.name}이 배가 고파 식량을 찾습니다 🍚")
		elif self.sleepiness > 80:
			self.task = "rest"
			add_log(f"{self.name}은 피곤해서 쉬고 있습니다 😴")
		elif self.belonging < 40:
			self.task = "talk"
			add_log(f"{self.name}은 외로워서 대화를 찾습니다 🗣️")
		else:
			if random.random() < 0.1:
				self.task = "farm"
				add_log(f"{self.name}은 농사를 시작합니다 🌾")

ai_agents = [
	AIAgent(1, "민아", "여", 50, 50),
	AIAgent(2, "지호", "남", 52, 50)
]

def ai_tick_all(delta_seconds=1):
	for ai in ai_agents:
		ai.tick(delta_seconds)
