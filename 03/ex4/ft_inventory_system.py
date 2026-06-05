import sys


def add_inventory(inventory: dict, word: str, value: str) -> dict:
    try:
        key = str(word)
        number = int(value)
        inventory.update({key: number})
    except ValueError as error:
        print("Invalid input: ", error)
    return inventory


def find_max(glo: dict) -> dict:
    seen: dict = {}
    i: int = 0
    for y in glo:
        if glo[y] > i:
            seen = y
        i = glo[y]
    return seen


def find_min(glo: dict) -> dict:
    seen: dict = {}
    i: int = glo[0]
    for y in glo:
        if glo[y] < i:
            seen = y
        i = glo[y]
    return seen


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict = {}
    discard: list = []
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
    print(f"Item list: {dict.keys(inventory)}")
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
        print(f"Most abundant item: {find_max(inventory)}"
              f" with a quantity of {find_max(inventory)[0]}")
        print(f"Least abundant item: {find_min(inventory)}"
              f" with a quantity of {find_min(inventory)[0]}")
    inventory = add_inventory(inventory, "mace", "3")
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
