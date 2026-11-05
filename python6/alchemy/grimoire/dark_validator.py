from .dark_spellbook import (
    dark_spell_allowed_ingredients,
)  # Top-level import causes circular import failure


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()

    if any(item.lower() in lower_ingredients for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
