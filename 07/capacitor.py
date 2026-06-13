from ex1 import HealingCreatureFactory, TransformCreatureFactory


def heal_factory_checker(object: HealingCreatureFactory) -> None:
    try:
        obj1 = object.create_base()
        obj2 = object.create_evolved()
    except ValueError:
        print("Error")
        return
    message1: str = obj1.describe()
    message2: str = obj1.attack()
    message3: str = obj1.heal("itself")
    message4: str = obj2.describe()
    message5: str = obj2.attack()
    message6: str = obj1.heal("itself and others")
    print("\tbase:")
    print(message1)
    print(message2)
    print(message3)
    print("\tevolved:")
    print(message4)
    print(message5)
    print(message6)


def transform_factory_checker(object: TransformCreatureFactory) -> None:
    try:
        obj1 = object.create_base()
        obj2 = object.create_evolved()
    except ValueError:
        print("Error")
        return
    message1: str = obj1.describe()
    message2: str = obj1.attack()
    message3: str = obj1.transform()
    message4: str = obj1.attack()
    message5: str = obj1.revert()
    message6: str = obj2.describe()
    message7: str = obj2.attack()
    message8: str = obj2.transform()
    message9: str = obj2.attack()
    message10: str = obj2.revert()
    print("\tbase:")
    print(message1)
    print(message2)
    print(message3)
    print(message4)
    print(message5)
    print("\tevolved:")
    print(message6)
    print(message7)
    print(message8)
    print(message9)
    print(message10)


def main() -> None:
    factory1 = HealingCreatureFactory()
    factory2 = TransformCreatureFactory()
    print("Testing Creature with healing capability")
    heal_factory_checker(factory1)
    print()
    print("Testing Creature with transform capability")
    transform_factory_checker(factory2)


if __name__ == "__main__":
    main()
