logs = []
def add_log(msg):
	if len(logs) > 100:
		logs.pop(0)
	logs.append(msg)

def get_logs():
	return logs[::-1]

class AIAgent:
	def __init__(self, name, age=20):
		self.name = name
		self.age = age
		self.task = "idle"
		self.hunger = 100
		self.inventory = {"wood": 0, "stone": 0, "food": 0}

	def tick(self):
		self.hunger -= 1
		if self.hunger < 50:
			self.task = "gathering"
			self.inventory["food"] += 1
			self.hunger += 10
			add_log(f"{self.name}이 식량을 채집했습니다 🍎")
		else:
			self.task = "resting"
			add_log(f"{self.name}은 휴식을 취합니다 💤")

	def get_status(self):
		return {
			"name": self.name,
			"age": self.age,
			"hunger": self.hunger,
			"task": self.task,
			"inventory": self.inventory
		}

agents = [AIAgent("민아이"), AIAgent("지호이")]

def get_agents():
	for agent in agents:
		agent.tick()
	return [a.get_status() for a in agents]

class Village:
	def __init__(self, name):
		self.name = name
		self.resources = {"wood": 0, "stone": 0, "food": 0}

class City:
	def __init__(self, name):
		self.name = name
		self.villages = []

class Nation:
	def __init__(self, name):
		self.name = name
		self.cities = []

v1 = Village("숲마을")
v2 = Village("강마을")
c1 = City("그린시티")
c1.villages.extend([v1, v2])
nation = Nation("에코리아")
nation.cities.append(c1)

def get_nation_structure():
	return {
		"nation": nation.name,
		"cities": [
			{
				"name": c.name,
				"villages": [{"name": v.name, "resources": v.resources} for v in c.villages]
			}
			for c in nation.cities
		]
	}
