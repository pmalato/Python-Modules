from functools import reduce, partial, lru_cache, singledispatch
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
        print("Non-existing Key: ", e)
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
    @singledispatch
    def base_spell(spell: Any) -> Any:
        return f"Unknown spell type: {spell}"

    @base_spell.register(int)
    def damage_spell(spell: int) -> int:
        return spell

    @base_spell.register(str)
    def enchantment(spell: str) -> str:
        return f"{spell}"

    @base_spell.register(list)
    def multi_cast(spell: list) -> list:
        return [x for x in spell]
    return base_spell


def main() -> None:
    print("\nTesting spell reducer...")
    operation_list = [1, 2, 3, 4, 5]
    print("Addition", spell_reducer(operation_list, "add"))
    print("Multiplication", spell_reducer(operation_list, "multiply"))
    print("Max", spell_reducer(operation_list, "max"))
    print("Min", spell_reducer(operation_list, "min"))
    print("Unknown", spell_reducer(operation_list, "cowabanga"))
    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{power} {element} {target}"
    enchant = partial_enchanter(base_enchantment)
    print(enchant["Geo"](target="Zhongli"))
    print(enchant["Cryo"](target="Sandrone"))
    print("\nTesting memoized fibonacci...")
    print(memoized_fibonacci(35))
    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(45))
    print(spell("Wazaaaaaa"))
    print(spell(["crazy", "people", "are", "the", "best"]))
    print(spell({"something": 67}))


if __name__ == "__main__":
    main()
