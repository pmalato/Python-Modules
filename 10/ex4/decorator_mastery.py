from collections.abc import Callable
from functools import wraps
from time import perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(func: Callable) -> Callable:
        start = perf_counter()
        print(f"Casting function_name... {spell_timer.__name__}")
        end = perf_counter()
        result = func(*args, **kwargs)
        print(f"Spell completed in {(start - end):.3f} seconds")
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(min_power: Callable) -> Callable:
        @wraps(min_power)
        def wrapper(min_power: Callable) -> Callable:
            ...


def retry_spell(max_attempts: int) -> Callable:
    ...


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...

    def cast_spell(self, spell_name: str, power: int) -> str:
        ...


def main() -> None:
    print("\nTesting spell timer...")
    wrapper = spell_timer(3)
    print(wrapper(3))
    print("\nTesting spell timer...")
    print("\nTesting spell timer...")
    print("\nTesting spell timer...")


if __name__ == "__main__":
    main()
