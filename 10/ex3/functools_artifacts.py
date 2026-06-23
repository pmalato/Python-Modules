from functools import reduce, partial, lru_cache
from collections.abc import Callable
from operator import mul, add
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells == []:
        return 0
    operations = {
        "add": reduce(add, spells),
        "multiply": reduce(mul, spells),
        "max": max(spells),
        "min": min(spells)
    }
    try:
        return operations[operation]
    except KeyError as e:
        print("Error: ", e)
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    dendro_enchant = partial(base_enchantment, power=50, element="Dendro")
    cryo_enchant = partial(base_enchantment, power=50, element="Cryo")
    geo_enchant = partial(base_enchantment, power=50, element="Geo")
    return {
        "Dendro": dendro_enchant,
        "Cryo": cryo_enchant,
        "Geo": geo_enchant
    }


@lru_cache(maxsize=128, typed=False)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    return spell_dispatcher


def main() -> None:
    print("\nTesting spell reducer...")
    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{power} {element} {target}"
    enchant = partial_enchanter(base_enchantment)
    print(enchant["Geo"](target="Zhongli"))
    print(enchant["Cryo"](target="Sandrone"))
    print("\nTesting memoized fibonacci...")
    print(memoized_fibonacci(35))
    print("\nTesting spell dispatcher...")


if __name__ == "__main__":
    main()
