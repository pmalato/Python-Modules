import sys


def main() -> None:
    args: int = len(sys.argv)
    if args != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        x = sys.argv[1]
        try:
            print(f"Accessing file: '{x}'")
            file = open(x)
            print("---")
            print(file.read())
            print("---")
            file.close()
            print(f"File '{x}' is closed.")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error opening file '{x}':", error)


if __name__ == "__main__":
    main()
