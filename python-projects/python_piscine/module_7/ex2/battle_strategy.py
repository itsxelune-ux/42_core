from abc import ABC, abstractmethod


class ABattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature) -> None:
        ...
