from ex1.capabilities import HealCapability, TransformCapability
from .battle_strategy import ABattleStrategy
from .exceptions import InvalidStrategyError


class NormalStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )

        print(creature.attack())


class AggressiveStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                (
                    f"Invalid Creature '{creature.name}' "
                    "for this aggressive strategy"
                )
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                (
                    f"Invalid Creature '{creature.name}' "
                    "for this defensive strategy"
                )
            )

        print(creature.attack())
        print(creature.heal())
