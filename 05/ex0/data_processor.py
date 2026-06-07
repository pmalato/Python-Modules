from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        raise NotImplementedError


class NumericProcessor(DataProcessor):
    _raw_data: int | float | list[int | float]
    _processed_data: str

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        return accept_ingestion

    def ingest(self, data: int | float | list[int | float]) -> None:
        self._raw_data = data
        if isinstance(data, list):
            self._processed_data = [str(elem) for elem in data]
        else:
            self._processed_data = str(data)
        super().output()


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        ...


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        ...


def main() -> None:
    print("=== Code Nexus - Data Processor ===")


if __name__ == "__main__":
    main()
