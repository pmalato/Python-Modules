from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
