import sys


def main() -> None:
    i: int = len(sys.argv)
    n: int = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    while n < (i):
        print(f"Argument {n}: {sys.argv[n]}")
        n += 1
    if i == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {i - 1}")
    print(f"Total arguments: {i}")


if __name__ == "__main__":
    main()
