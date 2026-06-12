from abc import ABC, abstractmethod


class Creature(ABC):
    def _init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self._name} uses Ember!"
        return phrase


class Pyrodon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self._name} uses Flamethrower!"
        return phrase


class Aquabub(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self._name} uses Water Gun!"
        return phrase


class Torragon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self._name} uses Hydro Pump!"
        return phrase
