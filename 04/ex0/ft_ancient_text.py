import sys
# import typing


def main() -> None:
    args: int = len(sys.argv)
    if args == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        for x in sys.argv:
            if x == sys.argv[0]:
                continue
            try:
                print(f"Accessing file: '{x}'")
                file = open(x)
                print("---")
                print(file.read())
                print("---")
                file.close()
                print(f"File {x} is closed.")
            except (FileNotFoundError, PermissionError) as error:
                print(f"Error opening file {x}:", error)


if __name__ == "__main__":
    main()
