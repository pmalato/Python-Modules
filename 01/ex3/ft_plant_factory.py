class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self) -> float:
        self.height += 0.8
        return self.height

    def age(self) -> int:
        self.day += 1
        return self.day

    def show(self) -> None:
        print(
                f"Created: {self.name}: {self.height:.1f}cm,"
                f"{self.day} days old")


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
