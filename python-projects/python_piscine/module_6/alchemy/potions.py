from .elements import create_air, create_earth
import elements


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"'{elements.create_fire()}' and "
        f"'{elements.create_water()}'"
    )
