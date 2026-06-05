from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    names: list = [
        "Theodore", "Aurora", "Leonid",
        "Carmen", "Gil", "Nico", "Juan",
        "Mary", "Barnabas", "Jack"]
    actions: list = [
        "play", "crawl", "scream",
        "think", "fall", "kick", "sail",
        "row", "cartwheel", "spray"]
    while True:
        r1: str = random.choice(names)
        r2: str = random.choice(actions)
        event: tuple = (r1, r2)
        yield event


def consume_event(series: list) -> Generator[tuple[str, str], None, None]:
    while series:
        i: int = random.randint(0, len(series) - 1)
        r3: tuple = series[i]
        del series[i]
        yield r3


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for x in range(1, 1001):
        something: tuple = next(event_gen)
        print(f"Event {x}: Player {something[0]} did action {something[1]}")
    sequence: list = []
    for y in range(1, 11):
        element: tuple = next(event_gen)
        sequence += [element]
    print(f"Built list of 10 events: {sequence}")
    for z in consume_event(sequence):
        print(f"Got event from list: {z}")
        print(f"Remains in list: {sequence}")


if __name__ == "__main__":
    main()
