from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self._type = type
        super().__init__()

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Ember!"
        return phrase


class Pyrodon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Flamethrower!"
        return phrase


class Aquabub(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Water Gun!"
        return phrase


class Torragon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        phrase: str = f"{self.name} uses Hydro Pump!"
        return phrase
