from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        flameling_obj = Flameling("Flameling", "Fire")
        return flameling_obj

    def create_evolved(self) -> Creature:
        pyrodon_obj = Pyrodon("Pyrodon", "Fire/Flying")
        return pyrodon_obj


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        aquabub_obj = Aquabub("Aquabub", "Water")
        return aquabub_obj

    def create_evolved(self) -> Creature:
        torragon_obj = Torragon("Torragon", "Water")
        return torragon_obj
