from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Any) -> None:
        ...
