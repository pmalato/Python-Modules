from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.battle_strategy import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidCreatureError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for x in range(len(opponents)):
        for y in range(x + 1, len(opponents)):
            obj1_c1, obj1_c2 = opponents[x]
            obj2_c1, obj2_c2 = opponents[y]
            creature1 = obj1_c1.create_base()
            creature2 = obj2_c1.create_base()
            print("\t* Battle *")
            print(creature1.describe())
            print("\tvs")
            print(creature2.describe())
            print("\t Now FIGHT!")
            try:
                obj1_c2.act(creature1)
                obj2_c2.act(creature2)
            except InvalidCreatureError as error:
                print("Battle error, aborting tournament:", error)


def main() -> None:
    factory1 = FlameFactory()
    factory2 = AquaFactory()
    factory3 = HealingCreatureFactory()
    factory4 = TransformCreatureFactory()
    strategy1 = NormalStrategy()
    strategy2 = AggressiveStrategy()
    strategy3 = DefensiveStrategy()
    combatents1: list = [
        (factory1, strategy1),
        (factory3, strategy3)]
    combatents2: list = [
        (factory1, strategy2),
        (factory3, strategy3)]
    combatents3: list = [
        (factory2, strategy1),
        (factory3, strategy3),
        (factory4, strategy2)]
    print("Tournament 0 (basic)")
    print("\t[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(combatents1)} opponents involved\n")
    battle(combatents1)
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(combatents2)} opponents involved\n")
    battle(combatents2)
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(combatents3)} opponents involved\n")
    battle(combatents3)


if __name__ == "__main__":
    main()
