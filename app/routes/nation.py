from fastapi import APIRouter
from app.services.init_sample import create_sample_structure

router = APIRouter()

nation = create_sample_structure()

@router.get("/api/nation")
def get_nation_structure():
    return {
        "nation": nation.name,
        "resources": nation.resources,
        "cities": [
            {
                "name": city.name,
                "resources": city.resources,
                "villages": [
                    {
                        "name": village.name,
                        "resources": village.resources,
                        "members": village.members
                    }
                    for village in city.villages
                ]
            }
            for city in nation.cities
        ]
    }
