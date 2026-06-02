def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            print(1 / 0)
        case 2:
            t = open("/nao/ha/aqui/nada")
            t.close()
        case 3:
            print(1 + "abc")  # type: ignore[operator]
        case _:
            print("Operation completed successfully\n")


def test_operations() -> None:
    for i in range(5):
        print(f"Testing operation {i} ...")
        try:
            garden_operations(i)
        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            FileNotFoundError
        ) as error:
            print(f"Caught {type(error).__name__}:", error)
    print("All types tested successfully!")


def main() -> None:
    print("=== Garden Errors Type Demo ===")
    test_operations()


if __name__ == "__main__":
    main()
