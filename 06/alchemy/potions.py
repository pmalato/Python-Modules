from .elements import create_air
from .elements import create_earth
from elements import create_fire
from elements import create_water


def healing_potion() -> str:
    phrase: str = (
        f"Healing potion brewed with'{create_fire()}' and '{create_water()}'")
    return phrase


def strength_potion() -> str:
    phrase: str = (
        f"Strength potion brewed with '{create_earth()}' and '{create_air()}'"
    )
    return phrase
