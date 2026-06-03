import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list = []
    invalid: list = []
    for x in sys.argv[1:]:
        try:
            scores = scores + [int(x)]
        except ValueError:
            invalid = invalid + [x]
    if scores != []:
        total = sum(scores)
        players = len(sys.argv) - 1
        average = total / players
        high = max(scores)
        low = min(scores)
        range = high - low
        print(f"Scores processed: {scores}")
        print(f"Total players: {players}")
        print(f"Total score: {total}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {range}")
    else:
        for x in invalid:
            print(f"Invalid parameter: '{x}'")
        print("No scores provided!"
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
