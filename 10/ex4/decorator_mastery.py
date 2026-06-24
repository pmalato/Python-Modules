from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any
from inspect import signature


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = perf_counter()
        print(f"Casting function_name... {func.__name__}")
        end = perf_counter()
        result = func(*args, **kwargs)
        print(f"Spell completed in {(start - end):.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*arg, **kwargs) -> Any:
            sig = signature(func)
            bound = sig.bind(*arg, **kwargs)
            power = bound.arguments["power"]
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*arg, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for x in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if not x == max_attempts - 1:
                        print(
                            "Spell failed, retrying... attempt"
                            f" {(x + 1)}/{max_attempts}")
            return ("Spell casting failed"
                    f" after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3 and all((x.isalpha() or x == " ") for x in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @power_validator(50)
    def my_power(power: int, type: str) -> str:
        return f"I have {power} lvl of {type} spell"

    @spell_timer
    def phrase(phrase: str) -> str:
        return phrase

    @retry_spell(5)
    def wrong_input(num: int) -> int:
        return num * num

    print("\nTesting spell timer...")
    print(phrase("Hello my beautiful friends!\n"))
    print(phrase("What have you been up to?\n"))
    print(phrase("I Don't like potatoes, unless they're chips!"))
    print("\nTesting power validator...")
    print("Validated: ", my_power(80, "Fire"))
    print("Invalid: ", my_power(30, "Ice"))
    print("\nTesting retry spell...")
    number: int = 90
    print(f"{number}")
    words: int = wrong_input("Incorrect spell")
    print(f"{words}")
    print("\nTesting spell timer...")
    mage_guild = MageGuild()
    print(mage_guild.cast_spell("Intense circle", 5))
    print(mage_guild.cast_spell("Intense circle", 10))
    print(mage_guild.cast_spell("Intense circle", 20))


if __name__ == "__main__":
    main()
