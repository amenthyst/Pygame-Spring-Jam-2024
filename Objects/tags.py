from abc import ABC, abstractmethod


class Damageable(ABC):
    @abstractmethod
    def damage(self, amount: int):
        pass