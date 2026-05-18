class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self._name = name
        self._height = self.set_height(height)
        self._day = self.set_age(day)

    def grow(self) -> float:
        self._height += 0.8
        return self._height

    def age(self) -> int:
        self._day += 1
        return self._day

    def set_height(self, nb) -> float:
        if nb < 0.0:
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
        print(
                f"Created: {self._name}: {self._height:.1f}cm,"
                f"{self._day} days old")


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
