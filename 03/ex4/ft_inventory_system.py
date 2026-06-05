import sys


def add_inventory(inventory: dict, word: str, value: str) -> dict:
    try:
        key = str(word)
        number = int(value)
        inventory.update({key: number})
    except ValueError as error:
        print("Invalid input: ", error)
    return inventory


def find_max(glossary: dict[str, int]) -> dict:
    item_name = None
    amount = 0
    for y in glossary:
        if y is None or glossary[y] > amount:
            item_name = y
            amount = glossary[y]
    return {"name": item_name, "quantity": amount}


def find_min(glossary: dict[str, int]) -> dict:
    item_name = None
    amount = float('inf')
    for y in glossary:
        if y is None or glossary[y] < amount:
            item_name = y
            amount = glossary[y]
    return {"name": item_name, "quantity": amount}


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    discard: list[str] = []
    count: int = 0
    amount: int = 0
    percentage: float
    for arg in sys.argv:
        if ":" in arg:
            try:
                key, svalue = arg.split(":", 1)
                value = int(svalue)
                if key not in inventory:
                    inventory[key] = value
                    count += 1
                else:
                    discard += [key]
            except ValueError as error:
                print("Invalid input: ", error)
    if discard:
        print(f"Redundant items: {discard} - discarding")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    if count > 0:
        for x in inventory:
            amount += inventory[x]
        print(f"Quantity of items the {count} items: {amount}")
        for y in inventory:
            try:
                percentage = float(inventory[y] / amount * 100)
                print(f"Item {y} represents {percentage:.2f}%")
            except ZeroDivisionError as error:
                print("Invalid input: ", error)
        high: dict[str, int] = find_max(inventory)
        low: dict[str, int] = find_min(inventory)
        print(f"Most abundant item: {high['name']}"
              f" with a quantity of {high['quantity']}")
        print(f"Least abundant item: {low['name']}"
              f" with a quantity of {low['quantity']}")
    inventory = add_inventory(inventory, "mace", "3")
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
