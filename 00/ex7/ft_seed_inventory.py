def ft_seed_inventory(vegetable: str, number: int, type: str) -> None:
    if type == "packets":
        print(f"{vegetable.capitalize()} seeds: {number} {type} available")
    elif type == "grams":
        print(f"{vegetable.capitalize()} seeds: {number} {type} total")
    elif type == "area":
        print(f"{vegetable.capitalize()} seeds: covers {number} square meters")
    else:
        print("Unknown unit type")
