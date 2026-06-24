from typing import Any

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_healing() -> None:
    print("Testing Creature with healing capability")

    factory = HealingCreatureFactory()

    print("base:")
    creature: Any = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())

    print("evolved:")
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")

    factory = TransformCreatureFactory()

    print("base:")
    creature: Any = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())

    print("evolved:")
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


if __name__ == "__main__":
    test_healing()
    print()
    test_transform()
