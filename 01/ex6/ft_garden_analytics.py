class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = height
        self._day = day
        self._stats = Plant.Stats()

    class Stats:
        def __init__(self) -> None:
            self._cgrow = 0
            self._cage = 0
            self._cshow = 0

    def grow(self, nb) -> float:
        self._height += nb
        self._stats._cgrow += 1
        return self._height

    def age(self, nb) -> int:
        self._day += nb
        self._stats._cage += 1
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
    def one_year_check(nb) -> int:
        if nb > 365:
            print(f"is {nb} days more than a year? -> True")
            return True
        else:
            print(f"is {nb} days more than a year? -> False")
            return False

    @classmethod
    def anonymous(cls):
        return (cls("Unknown name", 0, 0))

    def show(self) -> None:
        self._stats._cshow += 1
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._day} days old")

    def stats_show(self) -> None:
        print(f"Stats: {self._stats._cgrow} grow,"
              f" {self._stats._cage} age, {self._stats._cshow} show")


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

    def color_check(self) -> None:
        print(f"Color: {self.color}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 day: int, color: str, cseed: int) -> None:
        super().__init__(name, height, day, color)
        self.seedcount = cseed
        self.seedsave = cseed

    def seed_show(self) -> None:
        if self.bloomed is False:
            self.seedcount = 0
        else:
            self.seedcount = self.seedsave
        print(f"Seeds: {self.seedcount}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 day: int, trunk_diameter: float) -> None:
        super().__init__(name, height, day)
        self.trunk_diameter = trunk_diameter
        self.nshade = 0

    def produce_shade(self) -> None:
        self.nshade += 1
        print(f"Tree {self._name} produces shade of {self._height:.1f}cm long"
              f" and {self.trunk_diameter:.1f}cm wide")

    def trunk_state(self) -> None:
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def shade_show(self) -> None:
        print(f"{self.nshade} shade")


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
    plant1 = Plant("Lily", 12, 30)
    plant2 = Plant("Daisy", 20, 400)
    plant1.one_year_check(plant1._day)
    plant2.one_year_check(plant2._day)
    print("\n")
    print("=== Flower")
    flower1 = Flower("Rose", 15, 10, "Red")
    flower1.show()
    flower1.color_check()
    flower1.bloom_state()
    flower1.stats_show()
    flower1.grow(8)
    flower1.bloom()
    flower1.show()
    flower1.color_check()
    flower1.stats_show()
    print("\n")
    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    tree1.trunk_state()
    tree1.stats_show()
    tree1.shade_show()
    tree1.produce_shade()
    tree1.stats_show()
    tree1.shade_show()
    print("\n")
    print("=== Seed")
    seed1 = Seed("Sunflower", 80, 45, "yellow", 42)
    seed1.show()
    seed1.color_check()
    seed1.bloom_state()
    seed1.seed_show()
    seed1.grow(30)
    seed1.age(20)
    seed1.bloom()
    seed1.show()
    seed1.color_check()
    seed1.bloom_state()
    seed1.seed_show()
    seed1.stats_show()
    print("\n")
    print("=== Anonymous")
    plant3 = Plant.anonymous()
    plant3.show()
    plant3.stats_show()


if __name__ == "__main__":
    main()
