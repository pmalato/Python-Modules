def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise ValueError(f"Testing operation {operation_number} ...\n")
    elif operation_number == 1:
        raise ZeroDivisionError(f"Testing operation {operation_number} ...\n")
    elif operation_number == 2:
        raise FileNotFoundError(f"Testing operation {operation_number} ...\n")
    elif operation_number == 3:
        raise TypeError(f"Testing operation {operation_number} ...\n")
    else:
        print("Operation completed successfully\n")


def test_operations() -> None:
    try:
        garden_operations(0)
    except ValueError as error:
        print("Caught ValueError:", error, "\n")
    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print("Caught ZeroDivisionError:", error, "\n")
    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error, "\n")
    try:
        garden_operations(3)
    except TypeError as error:
        print("Caught TypeError:", error, "\n")


def main() -> None:
    print("=== Garden Errors Type Demo ===")
    test_operations()


if __name__ == "__main__":
    main()
