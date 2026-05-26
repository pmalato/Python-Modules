def input_temperature(temp_str: str) -> int:
    temp_str = input("Input data is ")
    conv: int = int(temp_str)
    return conv

def test_temperature() -> None:
    try:
        input_temperature("25")

def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    test_temperature()


if __name__ == "__main__":
    main()
