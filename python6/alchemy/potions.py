import elements
from .elements import create_earth, create_air


def healing_potion() -> str:
    earth_result = create_earth()
    air_result = create_air()
    return f"Healing potion brewed with '{earth_result}' and '{air_result}'"


def strength_potion() -> str:
    fire_result = elements.create_fire()
    water_result = elements.create_water()
    return f"Strength potion brewed with '{fire_result}' and '{water_result}'"
