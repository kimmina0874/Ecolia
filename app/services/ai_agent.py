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

	def tick(self):
		if not self.is_alive:
			return

		self.age += 1
		self.energy -= 1 if not self.sick else 2

		# 질병 확률 (1%)
		if not self.sick and random.random() < 0.01:
			self.sick = True

		# 노화로 인한 자연사 확률 (5% 이상)
		if self.age > 100 and random.random() < 0.05:
			self.is_alive = False

		if self.energy <= 0:
			self.is_alive = False

		# 간단한 랜덤 이동
		self.x += random.choice([-1, 0, 1])
		self.y += random.choice([-1, 0, 1])

# 전역 에이전트 리스트
ai_agents = [
	AIAgent(id=1, x=100, y=100),
	AIAgent(id=2, x=120, y=100)
]

def ai_tick_all():
	for ai in ai_agents:
		ai.tick()

	# 번식 조건: 가까운 위치 + 개체수 제한
	if len(ai_agents) < 10:
		alive = [a for a in ai_agents if a.is_alive]
		for i, a1 in enumerate(alive):
			for a2 in alive[i+1:]:
				if abs(a1.x - a2.x) < 5 and abs(a1.y - a2.y) < 5:
					new_ai = AIAgent(id=len(ai_agents) + 1, x=a1.x, y=a1.y)
					ai_agents.append(new_ai)
					break
