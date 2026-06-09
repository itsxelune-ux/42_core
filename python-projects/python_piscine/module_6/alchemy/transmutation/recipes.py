from alchemy.elements import create_air
from elements import create_fire
from ..potions import strength_potion

def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    fire = create_fire()

    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{potion}' mixed with '{fire}'"
    )