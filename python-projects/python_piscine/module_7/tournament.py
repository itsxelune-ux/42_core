from ex0 import FlameFactory, AquaFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

            print()


def main():
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    battle(opponents)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    battle(opponents)

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    battle(opponents)


if __name__ == "__main__":
    main()
