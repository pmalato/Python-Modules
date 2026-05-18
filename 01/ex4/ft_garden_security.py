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

    def set_height(self, nb) -> float:
        if nb < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = nb
            print(f"Height updated: {self.height:.1f}cm")
        return self.height

    def set_age(self, nb) -> int:
        if nb < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Height update rejected")
        else:
            self.day = round(nb)
            print(f"Age updated: {self.day} days")
        return self.day

    def get_height(self) -> None:
        print(f"Current height: {self.height:.1f}cm")

    def get_age(self) -> None:
        print(f"Current age: {self.day} days old")

    def state_check(self) -> None:
        print(
                f"Current state: {self.name}: {self.height:.1f}cm, "
                f"{self.day} days old")

    def show(self) -> None:
        print(
                f"Created: {self.name}: {self.height:.1f}cm,"
                f"{self.day} days old")


def main() -> None:
    print("=== Garden Secuity System ===")
    plant1 = Plant("Rose", 15, 10)
    plant1.show()
    print("\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-25)
    plant1.set_age(-30)
    print("\n")
    plant1.state_check()


if __name__ == "__main__":
    main()
