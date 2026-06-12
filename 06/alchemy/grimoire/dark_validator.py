from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    if dark_spell_allowed_ingredients().__contains__(ingredients):
        return "VALID"
    else:
        return "INVALID"
