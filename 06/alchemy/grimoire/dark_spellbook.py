from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    phrase: str = (
        f"Spell record: {spell_name} {validate_ingredients(ingredients)}")
    return phrase
