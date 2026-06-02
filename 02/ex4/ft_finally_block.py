class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    try:
        water_plant("Lettuce")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    try:
        water_plant("Carrots")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    try:
        water_plant("lettuce")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
