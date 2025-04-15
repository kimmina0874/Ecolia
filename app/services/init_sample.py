from app.models.nation import Nation, City, Village

def create_sample_structure():
    nation = Nation("에코리아")
    city1 = City("그린시티")
    village1 = Village("숲마을")
    village2 = Village("강마을")
    city1.add_village(village1)
    city1.add_village(village2)
    nation.add_city(city1)

    city2 = City("스톤시티")
    village3 = Village("산마을")
    city2.add_village(village3)
    nation.add_city(city2)

    return nation
