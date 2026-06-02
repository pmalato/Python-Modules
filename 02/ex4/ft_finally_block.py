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
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        valid_vegs = {"Tomato", "Lettuce", "Carrots"}
        for veggie in valid_vegs:
            water_plant(veggie)
    except PlantError as error:
        print("Caught PlantError:", error)
    finally:
        print("Close watering system")
    print()
    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        invalid_vegs = {"Tomato", "lettuce", "Carrot"}
        for veggie in invalid_vegs:
            water_plant(veggie)
    except PlantError as error:
        print("Caught PlantError:", error)
    finally:
        print("Close watering system\n")
        print("Cleanup always happens, even when there's an error")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
