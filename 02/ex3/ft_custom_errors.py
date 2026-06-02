class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def input_plant(age: int) -> None:
    if age < 40:
        raise PlantError("Tomato is still growing!")
    elif age > 60:
        raise PlantError("Tomato is wilting!")


def input_water(water: float) -> None:
    if water < 2.5:
        raise WaterError("Not enough water in the tank!")
    elif water > 5.5:
        raise WaterError("Too much water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        input_plant(69)
    except PlantError as error:
        print("Caught PlantError:", error, "\n")
    print("Testing WaterError...")
    try:
        input_water(7.3)
    except WaterError as error:
        print("Caught WaterError:", error, "\n")
    print("Testing GardenError...")
    try:
        input_plant(69)
    except GardenError as error:
        print("Caught GardenError:", error)
    try:
        input_water(7.3)
    except GardenError as error:
        print("Caught GardenError:", error)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
