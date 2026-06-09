def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]

    ingredients_lower = ingredients.lower()

    if any(a in ingredients_lower for a in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"