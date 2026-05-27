def input_temperature(temp_str: str) -> int:
    conv: int = int(temp_str)
    print(f"Temperature is now {conv}°C\n")
    return conv


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as error:
        print("Input data is '25'")
        print("Caught input_temperature error:", error, "\n")
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
