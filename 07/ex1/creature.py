from .capability import HealCapability, TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Vine Whip!"
        return phrase

    def heal(self, target: str) -> str:
        phrase: str = f"{self.name} heals {target} for a small amount"
        return phrase


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Petal Dance!"
        return phrase

    def heal(self, target: str) -> str:
        phrase: str = (
            f"{self.name} heals {target} for a small amount"
            )
        return phrase


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str
        if self._transformed is False:
            phrase = f"{self.name} attacks normally."
        else:
            phrase = f"{self.name} performs a boosted strike!"
        return phrase

    def transform(self) -> str:
        self._transformed = True
        phrase: str = f"{self.name} shifts into a sharper form!"
        return phrase

    def revert(self) -> str:
        self._transformed = False
        phrase: str = f"{self.name} returns to normal."
        return phrase


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str
        if self._transformed is False:
            phrase = f"{self.name} attacks normally."
        else:
            phrase = f"{self.name} unleashes a devastating morph strike!"
        return phrase

    def transform(self) -> str:
        self._transformed = True
        phrase: str = f"{self.name} shifts into a dragonic battle form!"
        return phrase

    def revert(self) -> str:
        self._transformed = False
        phrase: str = f"{self.name} stabilizes its form."
        return phrase
