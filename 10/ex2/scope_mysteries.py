from collections.abc import Callable


def mage_counter() -> Callable:
    x: int = 0

    def func_help() -> int:
        nonlocal x
        x += 1
        return x
    return func_help


def spell_accumulator(initial_power: int) -> Callable:
    y = initial_power

    def func_help() -> int:
        nonlocal y
        y += initial_power
        return y
    return func_help


def enchantment_factory(enchantment_type: str) -> Callable:
    def func_help(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return func_help


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, value: int) -> dict[str, int]:
        nonlocal storage
        storage |= {key: value}
        return storage

    def recall(key: str) -> int | dict[str, str]:
        try:
            return storage[key]
        except KeyError:
            return {"unknown": "Memory not found"}
    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    count = mage_counter()
    print(count())
    print(count())
    print(count())
    print("\nTesting spell accumulator...")
    power = spell_accumulator(3)
    print(power())
    print(power())
    print(power())
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory("Fire")
    print(enchantment1("Sword"))
    enchantment2 = enchantment_factory("Frost")
    print(enchantment2("Bow"))
    enchantment3 = enchantment_factory("Mystic")
    print(enchantment3("Catalyst"))
    print("\nTesting memory vault...")
    mess = memory_vault()
    print("Store: ", mess["store"]("something", 30))
    print("Recall: ", mess["recall"]("something"))
    print("Recall: ", mess["recall"]("something else"))


if __name__ == "__main__":
    main()
