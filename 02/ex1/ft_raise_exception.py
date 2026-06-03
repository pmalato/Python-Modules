class WrgTemper(BaseException):
    pass


def input_temperature(temp_str: str) -> int:
    conv: int = int(temp_str)
    if conv < 0:
        raise WrgTemper(f"{conv}°C is too cold for plant (0°C)")
    elif conv > 40:
        raise WrgTemper(f"{conv}°C is too hot for plant (40°C)")
    print(f"Temperature is now {conv}°C\n")
    return conv


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as error:
        print("Input data is 'abc'")
        print("Caught input_temperature error:", error, "\n")
    try:
        input_temperature("100")
    except WrgTemper as error:
        print("Input data is '100'")
        print("Caught input_temperature error:", error, "\n")
    try:
        input_temperature("-50")
    except WrgTemper as error:
        print("Input data is '-50'")
        print("Caught input_temperature error:", error, "\n")
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
