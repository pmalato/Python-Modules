from elements import create_fire
from alchemy import elements
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
	return f"Recipe transmuting Lead to Gold: "\
		f"brew '{elements.create_air()}' and "\
			f"'{strength_potion()}' mixed with '{create_fire()}'"