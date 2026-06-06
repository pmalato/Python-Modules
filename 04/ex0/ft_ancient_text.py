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
        except OSError as error:
            print(f"Error opening file '{x}':", error)
            return
        try:
            print("---")
            print(file.read())
            print("---")
        except OSError as error:
            print(f"Error opening file '{x}':", error)
        finally:
            file.close()
            print(f"File '{x}' is closed.")


if __name__ == "__main__":
    main()
