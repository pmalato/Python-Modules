from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory_checker(object: CreatureFactory) -> bool:
    if object.create_base() and object.create_evolved():
        return True


def main() -> None:
    obj1 = FlameFactory()
    obj2 = AquaFactory()
    show1 = obj1.create_base()
    show2 = obj1.create_evolved()
    print("Testing factory")
    print(show1)
    print(show2)
    print()
    show3 = obj2.create_base()
    show4 = obj2.create_evolved()
    print("Testing factory")
    print(show3)
    print(show4)


if __name__ == "__main__":
    main()
