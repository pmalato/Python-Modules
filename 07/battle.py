from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory_checker(object: CreatureFactory) -> None:
    try:
        obj1 = object.create_base()
        obj2 = object.create_evolved()
    except ValueError:
        print("Error")
        return
    message1: str = obj1.describe()
    message2: str = obj1.attack()
    message3: str = obj2.describe()
    message4: str = obj2.attack()
    print(message1)
    print(message2)
    print(message3)
    print(message4)


def base_fight(object2: FlameFactory, object3: AquaFactory) -> None:
    subject1 = object2.create_base()
    subject2 = object3.create_base()
    print(subject1.describe())
    print("\tvs")
    print(subject2.describe())
    print(subject1.attack())
    print(subject2.attack())


def main() -> None:
    ffactory = FlameFactory()
    afactory = AquaFactory()
    print("Testing factory")
    factory_checker(ffactory)
    print()
    print("Testing factory")
    factory_checker(afactory)
    print("\nTesting battle")
    base_fight(ffactory, afactory)


if __name__ == "__main__":
    main()
