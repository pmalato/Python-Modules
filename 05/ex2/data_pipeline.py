from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.processed_data: list[tuple[int, str]] = []
        self._rank: int = 0
        self._ingestion: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        pop_item = self.processed_data.pop(0)
        return pop_item

    def get_ingestion_count(self) -> int:
        return self._ingestion


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
        # print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if (isinstance(data, (int | float)) or
                (isinstance(data, list) and
                    all(isinstance(i, (int, float)) for i in data))):
            if isinstance(data, list):
                conv_list: list = [str(elem) for elem in data]
                for x in conv_list:
                    self.processed_data += [(self._rank, x)]
                    self._rank += 1
                    self._ingestion += 1
            elif isinstance(data, (int, float)):
                conv_num = str(data)
                self.processed_data += [(self._rank, conv_num)]
                self._rank += 1
                self._ingestion += 1
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
        # print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if isinstance(data, str) or \
            (isinstance(data, list) and
             all(isinstance(d, str) for d in data)):
            if isinstance(data, list):
                conv_text_list = data
                for z in conv_text_list:
                    self.processed_data += [(self._rank, z)]
                    self._rank += 1
                    self._ingestion += 1
            else:
                conv_text: str = data
                self.processed_data += [(self._rank, conv_text)]
                self._rank += 1
                self._ingestion += 1
        else:
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
        # print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if self.is_datatype_valid(data):
            if self.is_datatype_list(data):
                conv_list_dict = data
                for n in conv_list_dict:
                    dict_to_str = ": ".join(n.values())
                    self.processed_data += [(self._rank, dict_to_str)]
                    self._rank += 1
                    self._ingestion += 1
            elif self.is_datatype_dict(data):
                conv_dict = data
                for m in conv_dict:
                    self.processed_data += [(self._rank, conv_dict[m])]
                    self._rank += 1
                    self._ingestion += 1
        else:
            raise ValueError


class DataStream():
    def __init__(self) -> None:
        self._proccess: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proccess.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for elm in stream:
            check: bool = False
            for case in self._proccess:
                try:
                    if case.validate(elm):
                        case.ingest(elm)
                        check = True
                except ValueError as error:
                    print("DataStream error - ", error)
            if check is False:
                print(f"Data Stream error - "
                      f"can't process element in stream '{elm}'")

    def print_processors_stats(self) -> None:
        count: int = 0
        if self._proccess == []:
            print("No processor found, no data")
        else:
            for t in self._proccess:
                count = t.get_ingestion_count()
                print(f"{t.__class__.__name__}: total {count} items processed,"
                      f" remaining {len(t.processed_data)}")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    print("== DataStream statistics ==")
    ds1 = DataStream()
    ds1.print_processors_stats()
    st_list1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
          'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
    print("\nRegistering Numeric Processor")
    num1 = NumericProcessor()
    print(f"\nSend first batch of data on stream: {st_list1}")
    ds1.register_processor(num1)
    ds1.process_stream(st_list1)
    print("== DataStream statistics ==")
    ds1.print_processors_stats()
    print("\nRegistering other data processors")
    text1 = TextProcessor()
    log1 = LogProcessor()
    ds1.register_processor(text1)
    ds1.register_processor(log1)
    print("Send the same batch again")
    ds1.process_stream(st_list1)
    print("== DataStream statistics ==")
    ds1.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    num1.output()
    num1.output()
    num1.output()
    text1.output()
    text1.output()
    log1.output()
    ds1.print_processors_stats()


if __name__ == "__main__":
    main()
