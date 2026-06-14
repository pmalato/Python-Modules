from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability


class InvalidCreatureError(Exception):
    ...


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{creature.name}'"
                f" for this aggressive strategy")
        else:
            act1 = creature.attack()
            print(act1)

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{creature.name}'"
                f" for this aggressive strategy")
        else:
            transform_creature = cast(TransformCapability, creature)
            act1 = transform_creature.transform()
            act2 = creature.attack()
            act3 = transform_creature.revert()
            print(act1)
            print(act2)
            print(act3)

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{creature.name}'"
                f" for this aggressive strategy")
        else:
            heal_creature = cast(HealCapability, creature)
            act1 = creature.attack()
            act2 = heal_creature.heal("itself")
            print(act1)
            print(act2)

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
