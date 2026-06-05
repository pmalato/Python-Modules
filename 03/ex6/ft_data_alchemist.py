import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    names: list = [
        "Theodore", "aurora", "leonid",
        "Carmen", "Gil", "nico", "Juan",
        "mary", "Barnabas", "Jack"]
    force_cap: list = [str.capitalize(each) for each in names if each]
    n_cap: list = [elem for elem in names if elem != str.capitalize(elem)]
    name_dict: dict = {key: random.randint(1, 1000) for key in force_cap}
    score_list: list = []
    for x in name_dict:
        score_list += [name_dict[x]]
    # average_score: float =
    print(score_list)
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {force_cap}")
    print(f"New list of capitalized names only: {n_cap}")
    print(f"\nScore dict: {name_dict}")


if __name__ == "__main__":
    main()
