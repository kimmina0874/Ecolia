import random
from app.services.log_store import add_log

class AIAgent:
	def __init__(self, id, name, gender, x, y, age=20):
		self.id = id
		self.name = name
		self.gender = gender
		self.x = x
		self.y = y
		self.age = age
		self.hunger = 100
		self.energy = 100
		self.sleepiness = 0
		self.memory = {
			"find_fruit": {"success": 0, "fail": 0},
			"find_mushroom": {"success": 0, "fail": 0},
			"hunt": {"success": 0, "fail": 0},
			"gather_wood": {"success": 0, "fail": 0},
			"mine_stone": {"success": 0, "fail": 0},
			"explore": {"success": 0, "fail": 0}
		}
		self.task = "idle"
		self.inventory = {"fruit": 0, "mushroom": 0, "meat": 0, "wood": 0, "stone": 0}

	def tick(self):
		add_log(f"{self.name} 상태: hunger={self.hunger}, wood={self.inventory['wood']}, stone={self.inventory['stone']}")
		self.hunger -= 2
		self.sleepiness += 1

		if self.hunger < 40:
			self.task = self.choose_food_task()
		elif self.inventory["wood"] >= 10 and self.inventory["stone"] >= 5:
			self.task = "build_house"
		elif self.inventory["wood"] < 5:
			self.task = "gather_wood"
		elif self.inventory["stone"] < 3:
			self.task = "mine_stone"
		else:
			self.task = "idle"

		getattr(self, self.task)()

	def choose_food_task(self):
		scores = {
			k: v["success"] - v["fail"]
			for k, v in self.memory.items()
			if k in ["find_fruit", "find_mushroom", "hunt"]
		}
		return max(scores, key=scores.get)

	def find_fruit(self):
		if random.random() < 0.7:
			self.inventory["fruit"] += 1
			self.hunger += 10
			self.memory["find_fruit"]["success"] += 1
			add_log(f"{self.name}이 과일을 찾았습니다 🍎")
		else:
			self.memory["find_fruit"]["fail"] += 1
			add_log(f"{self.name}이 과일을 찾지 못했습니다 😓")

	def find_mushroom(self):
		if random.random() < 0.5:
			self.inventory["mushroom"] += 1
			self.hunger += 8
			self.memory["find_mushroom"]["success"] += 1
			add_log(f"{self.name}이 버섯을 채집했습니다 🍄")
		else:
			self.memory["find_mushroom"]["fail"] += 1
			add_log(f"{self.name}이 버섯을 못 찾았습니다 😓")

	def hunt(self):
		if random.random() < 0.4:
			self.inventory["meat"] += 1
			self.hunger += 15
			self.memory["hunt"]["success"] += 1
			add_log(f"{self.name}이 작은 동물을 사냥했습니다 🐇")
		else:
			self.memory["hunt"]["fail"] += 1
			add_log(f"{self.name}이 사냥에 실패했습니다 😢")

	def gather_wood(self):
		self.inventory["wood"] += 1
		self.memory["gather_wood"]["success"] += 1
		add_log(f"{self.name}이 나무를 모았습니다 🌲")

	def mine_stone(self):
		self.inventory["stone"] += 1
		self.memory["mine_stone"]["success"] += 1
		add_log(f"{self.name}이 돌을 채굴했습니다 🪨")

	def build_house(self):
		self.inventory["wood"] -= 10
		self.inventory["stone"] -= 5
		add_log(f"{self.name}이 집을 지었습니다 🏠")

	def idle(self):
		add_log(f"{self.name}이 휴식을 취하고 있습니다 🌤️")
ai_agents = [
	AIAgent(1, "지호", "남", 50, 50),
	AIAgent(2, "민아", "여", 52, 50)
]

def ai_tick_all():
	for ai in ai_agents:
		ai.tick()

def get_status(self):
	return {
		"name": self.name,
		"age": self.age,
		"hunger": self.hunger,
		"sleepiness": self.sleepiness,
		"task": self.task,
		"inventory": self.inventory
	}