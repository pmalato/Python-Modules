from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._processed_data: list[tuple[int, str]] = []
        self._rank: int = 0
        self._ingestion: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        pop_item = self._processed_data.pop(0)
        return pop_item

    def get_ingestion(self) -> int:
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
                    self._ingestion += 1
            elif isinstance(data, (int, float)):
                conv_num = str(data)
                self._processed_data += [(self._rank, conv_num)]
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
        print(f"Trying to validate input '{data}': {accept_ingestion}")
        return accept_ingestion

    def ingest(self, data: Any) -> None:
        if isinstance(data, str) or \
            (isinstance(data, list) and
             all(isinstance(d, str) for d in data)):
            if isinstance(data, list):
                conv_text_list: list = data
                for z in conv_text_list:
                    self._processed_data += [(self._rank, z)]
                    self._rank += 1
                    self._ingestion += 1
            else:
                conv_text: str = data
                self._processed_data += [(self._rank, conv_text)]
                self._rank += 1
                self._ingestion += 1
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
                    self._ingestion += 1
            elif self.is_datatype_dict(data):
                conv_dict = data
                for m in conv_dict:
                    self._processed_data += [(self._rank, conv_dict[m])]
                    self._rank += 1
                    self._ingestion += 1
        else:
            raise ValueError


class DataStream():
    def __init__(self) -> None:
        self._count: int = 0
        self._storage: Any
        self._proc_obj: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc_obj.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for elm in stream:
            check: bool = False
            for i in self._proc_obj:
                try:
                    if i.validate(elm):
                        i.ingest(elm)
                        check = True
                        self._count += 1
                except ValueError as error:
                    print("DataStream error - ", error)
            if check is False:
                print(
                    "DataStream error -"
                    f"Can't process element in stream: {elm}")

    def print_processors_stats(self) -> None:
        for t in self._proc_obj:
            p
        print(
            f"{self._proc_obj} : total "
            f"{self._count} items processed, remaining {len(self._proc_obj)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")


if __name__ == "__main__":
    main()
