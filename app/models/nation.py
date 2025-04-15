class Village:
    def __init__(self, name):
        self.name = name
        self.resources = {"wood": 0, "stone": 0, "food": 0}
        self.members = []

class City:
    def __init__(self, name):
        self.name = name
        self.villages = []
        self.resources = {"iron": 0, "tools": 0}

    def add_village(self, village):
        self.villages.append(village)

class Nation:
    def __init__(self, name):
        self.name = name
        self.cities = []
        self.resources = {"gold": 0, "population": 0}

    def add_city(self, city):
        self.cities.append(city)
