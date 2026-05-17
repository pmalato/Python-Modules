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
        print(f"{self.name}: {self.height:.1f}cm, {self.day} days old")


def main():
    plant1 = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    plant1.show()
    while plant1.day < 37:
        print(f"=== Day {plant1.day - 29} ===")
        plant1.height = plant1.grow()
        plant1.day = plant1.age()
        plant1.show()
    print(f"Growth this week: {plant1.height - 25:.1f}cm")


if __name__ == "__main__":
    main()
