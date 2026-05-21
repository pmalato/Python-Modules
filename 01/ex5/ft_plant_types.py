class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = height
        self._day = day

    def grow(self, nb) -> float:
        self._height += nb
        return self._height

    def age(self, nb) -> int:
        self._day += nb
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

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, day: int, color: str) -> None:
        super().__init__(name, height, day)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._day} days old")
        print(f"Color: {self.color}")
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

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._day} days old")
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 day: int, harvest_season: str) -> None:
        super().__init__(name, height, day)
        self.harvest_season = harvest_season
        self.starting_age = day

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._day} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutricional value: {self._day - self.starting_age}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1 = Flower("Rose", 15, 10, "red")
    flower1.show()
    flower1.bloom()
    flower1.show()
    print("\n")
    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    tree1.produce_shade()
    print("\n")
    print("=== Vegetable")
    vegetable1 = Vegetable("Tomato", 5, 10, "April")
    vegetable1.show()
    vegetable1.age(20)
    vegetable1.show()


if __name__ == "__main__":
    main()
