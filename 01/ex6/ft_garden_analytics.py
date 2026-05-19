class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = height
        self._day = day

    def grow(self) -> float:
        self._height += 0.8
        return self._height

    def age(self) -> int:
        self._day += 1
        return self._day

    def set_height(self, nb):
        if nb < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = nb
            print(f"Height updated: {self._height:.1f}cm")
        return self._height

    def set_age(self, nb) -> int:
        if nb < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Height update rejected")
        else:
            self._day = round(nb)
            print(f"Age updated: {self._day} days")
        return self._day

    def get_height(self) -> None:
        print(f"Current height: {self._height:.1f}cm")

    def get_age(self) -> None:
        print(f"Current age: {self._day} days old")

    def state_check(self) -> None:
        print(
                f"Current state: {self._name}: {self._height:.1f}cm, "
                f"{self._day} days old")

    @staticmethod
    def one_year_check(nb) -> bool:
        if nb > 1:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls):
        return (cls())

    def show(self) -> None:
        print(
                f"{self._name}: {self._height:.1f}cm,"
                f" {self._day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
        super().__init__(name, height, day)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def bloom_state(self) -> None:
        if self.bloomed is False:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is boolming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 day: int, trunk_diameter: float) -> None:
        super().__init__(name, height, day)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} produces shade of {self._height:.1f}cm long"
              f" and {self.trunk_diameter:.1f}cm wide")

    def trunk_state(self) -> None:
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 day: int, harvest_season: str) -> None:
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.nutricional_value = 0
        self.starting_age = day

    def harvest_timing(self) -> None:
        print(f"Harvest season: {self.harvest_season}")

    def nutricional_state(self) -> None:
        print(f"Nutricional value: {self.nutricional_value}")


def main() -> None:
    print("=== Garden Statistics ===")
    print("=== Check year-old")


if __name__ == "__main__":
    main()
