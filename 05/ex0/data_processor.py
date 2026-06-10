from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._processed_data: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        pop_item = self._processed_data.pop(0)
        return pop_item


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
                conv_list: list = [str(elem) for elem in data]
                for x in conv_list:
                    self._processed_data += [(self._rank, x)]
                    self._rank += 1
            elif isinstance(data, (int, float)):
                conv_num = str(data)
                self._processed_data += [(self._rank, conv_num)]
                self._rank += 1
        else:
            raise ValueError


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        if isinstance(data, str):
            accept_ingestion = True
        elif isinstance(data, list) and all(isinstance(d, str) for d in data):
            accept_ingestion = True
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if isinstance(data, str) or \
            (isinstance(data, list) and
             all(isinstance(d, str) for d in data)):
            if isinstance(data, list):
                conv_text_list = data
                for z in conv_text_list:
                    self._processed_data += [(self._rank, z)]
                    self._rank += 1
            else:
                conv_text: str = data
                self._processed_data += [(self._rank, conv_text)]
                self._rank += 1
        raise ValueError


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def is_datatype_dict(self, obj: Any) -> bool:
        is_expected: bool = False
        if isinstance(obj, dict) and \
            all(isinstance(a, str) and
                isinstance(b, str) for a, b in obj.items()):
            is_expected = True
        return is_expected

    def is_datatype_list(self, obj: Any) -> bool:
        is_acceptable: bool = False
        if isinstance(obj, list) and \
            all(isinstance(elem, dict)
                and all(isinstance(x, str) and
                        isinstance(v, str)
                        for x, v in elem.items()) for elem in obj):
            is_acceptable = True
        return is_acceptable

    def is_datatype_valid(self, obj: Any) -> bool:
        is_data_valid: bool = False
        if self.is_datatype_dict(obj) or self.is_datatype_list(obj):
            is_data_valid = True
        return is_data_valid

    def validate(self, data: Any) -> bool:
        accept_ingestion: bool = False
        if self.is_datatype_valid(data):
            accept_ingestion = True
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if self.is_datatype_valid(data):
            if self.is_datatype_list(data):
                conv_list_dict = data
                for n in conv_list_dict:
                    dict_to_str = ": ".join(n.values())
                    self._processed_data += [(self._rank, dict_to_str)]
                    self._rank += 1
            elif self.is_datatype_dict(data):
                conv_dict = data
                for m in conv_dict:
                    self._processed_data += [(self._rank, conv_dict[m])]
                    self._rank += 1
        else:
            raise ValueError


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
    try:
        num1.ingest(num_list)
    except ValueError:
        print("Got exception: Improper numeric data")
    print("Extracting 3 values...")
    tuple1: tuple = num1.output()
    tuple2: tuple = num1.output()
    tuple3: tuple = num1.output()
    print(f"numeric value {tuple1[0]}: {tuple1[1]}")
    print(f"numeric value {tuple2[0]}: {tuple2[1]}")
    print(f"numeric value {tuple3[0]}: {tuple3[1]}")
    print("\nTesting Text Processor...")
    text1 = TextProcessor()
    text1.validate(42)
    list1: list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {list1}")
    try:
        text1.ingest(list1)
    except ValueError:
        print("Got exception: Improper text data")
    print("Extracting 2 values...")
    tuple4: tuple = text1.output()
    tuple5: tuple = text1.output()
    print(f"numeric value {tuple4[0]}: {tuple4[1]}")
    print(f"numeric value {tuple5[0]}: {tuple5[1]}")
    print("Testing Log Processor...")
    log1 = LogProcessor()
    log1.validate("hello")
    list_dict: list[dict] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {list_dict}")
    try:
        log1.ingest(list_dict)
    except ValueError:
        print("Got exception: Improper log data")
    print("Extracting 2 values...")
    tuple6: tuple = log1.output()
    tuple7: tuple = log1.output()
    print(f"numeric value {tuple6[0]}: {tuple6[1]}")
    print(f"numeric value {tuple7[0]}: {tuple7[1]}")


if __name__ == "__main__":
    main()
