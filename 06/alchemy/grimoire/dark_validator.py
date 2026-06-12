from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    sep_ingredients: list = ingredients.split(" ")
    for x in sep_ingredients:
        if x.lower() in dark_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
