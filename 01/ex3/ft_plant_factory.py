class Plant:
    def __init__(
            self, name: str, starting_height: float,
            starting_age: int) -> None:
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def grow(self) -> float:
        self.starting_height += 0.8
        return self.starting_height

    def age(self) -> int:
        self.starting_age += 1
        return self.starting_age

    def show(self) -> None:
        print(
                f"Created: {self.name}: {self.starting_height:.1f}cm,"
                f"{self.starting_age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    main()
