def validate_ingredients(ingredients: str) -> str:
    # fn-local import breaks the circular dep: light_spellbook imports this
    # module at top level, so a module-level import back would explode like
    # the dark pair. At call time light_spellbook is fully initialized.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    if any(a in ingredients_lower for a in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID