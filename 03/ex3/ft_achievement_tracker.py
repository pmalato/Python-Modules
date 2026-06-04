import random


def gen_player_achievements() -> set:
    achievements: tuple = (
        "Improper retalition",
        "This is what I was meant to do. Right..?",
        "Shortcuts! Shortcuts! Shortcuts!",
        "With great power, ... wait, never mind",
        "The Depth Star",
        "Gott catch'em all!!!",
        "Couldn't have done it better myself",
        "Hah... funny.",
        "Are we there yet?",
        "Now we are free!")
    r1: int = random.randint(0, 9)
    player_achv: set = set()
    player_achv = set(random.sample(achievements, r1))
    return player_achv
