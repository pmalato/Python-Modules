import random


def gen_player_achievements() -> set:
    achievements: tuple = (
        "Improper retaliation",
        "This is what I was meant to do... right?",
        "I voted against shortcuts",
        "With great power... wait, nevermind",
        "The Depth Star",
        "Gotta catch'em all!!!",
        "Couldn't have done it better myself",
        "Hah... funny.",
        "Finders, keepers!",
        "Now we are free!")
    r1: int = random.randint(0, 9)
    player_achv: set = set()
    player_achv = set(random.sample(achievements, r1))
    return player_achv


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    achievements: tuple = (
        "Improper retaliation",
        "This is what I was meant to do... right..?",
        "I voted against shortcuts",
        "With great power... wait, nevermind",
        "The Depth Star",
        "Gotta catch'em all!!!",
        "Couldn't have done it better myself",
        "Hah... funny.",
        "Finders, keepers!",
        "Now we are free!")
    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()
    common_achv: set = alice.intersection(bob, charlie, dylan)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {achievements}")
    print(f"\nCommon achievements: {common_achv}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")
    print(f"Alice is missing: {alice.difference(achievements)}")
    print(f"Bob is missing: {bob.difference(achievements)}")
    print(f"Charlie is missing: {charlie.difference(achievements)}")
    print(f"Dylan is missing: {dylan.difference(achievements)}")


if __name__ == "__main__":
    main()
