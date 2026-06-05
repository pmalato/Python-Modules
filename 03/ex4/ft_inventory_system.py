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
    max_key = None
    max_value = float('inf')
    for y in glo:
        if y is None or glo[y] > max_value:
            max_key = y
            max_value = glo[y]
    return {max_key: max_value}


def find_min(glo: dict) -> dict:
    min_key = None
    min_value = float('inf')
    for y in glo:
        if y is None or glo[y] < min_value:
            min_key = y
            min_value = glo[y]
    return {min_key: min_value}


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
        high = find_max(inventory)
        low = find_min(inventory)
        print(f"Most abundant item: {high}"
              f" with a quantity of {high.values}")
        print(f"Least abundant item: {low}"
              f" with a quantity of {low.values}")
    inventory = add_inventory(inventory, "mace", "3")
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
