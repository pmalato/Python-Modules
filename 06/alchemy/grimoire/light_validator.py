from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    if light_spell_allowed_ingredients().__contains__(ingredients):
        return "VALID"
    else:
        return "INVALID"
