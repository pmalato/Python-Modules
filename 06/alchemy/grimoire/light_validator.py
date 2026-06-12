def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    sep_ingredients: list = ingredients.split(" ")
    for x in sep_ingredients:
        if x.lower() in light_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
