from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._processed_data: Any
        self._index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        pop_item: list = [self._index, self._processed_data[self._index]]
        self._index += 1
        return (pop_item[0], pop_item.pop(1))


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        if isinstance(data, (int | float)):
            accept_ingestion = True
        if (isinstance(data, list)
                and all(isinstance(i, (int, float)) for i in data)):
            accept_ingestion = True
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if (isinstance(data, (int | float)) or
                (isinstance(data, list) and
                    all(isinstance(i, (int, float)) for i in data))):
            if isinstance(data, list):
                self.processed_data = [str(elem) for elem in data]
            elif isinstance(data, (int, float)):
                self.processed_data = str(data)
        else:
            raise ValueError


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        if isinstance(data, str | list[str]):
            accept_ingestion = True
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if isinstance(data, str | list[str]):
            self.processed_data = data
        else:
            raise Exception


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        if isinstance(data, dict[str: str] | list[dict[str: str]]):
            accept_ingestion = True
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if isinstance(data, dict[str: str] | list[dict[str: str]]):
            if isinstance(list[dict[str: str]]):
                for x in data[::2]:
                    self.processed_data = {data[x]: data[x + 1]}
            else:
                self.processed_data = data
        else:
            raise Exception


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num1 = NumericProcessor()
    num1.validate(42)
    num1.validate("Hello")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num1.ingest("foo")
    except ValueError:
        print("Got exception: Improper numeric data")
    num_list: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_list}")
    print(f"Extracting 3 values...")
    tuple1: tuple = num1.output()
    tuple2: tuple = num1.output()
    tuple3: tuple = num1.output()
    print(f"numeric value:{tuple1}")
    print(f"numeric value:{tuple2}")
    print(f"numeric value:{tuple3}")


if __name__ == "__main__":
    main()
