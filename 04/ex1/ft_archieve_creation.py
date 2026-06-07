import sys


def main() -> None:
    args: int = len(sys.argv)
    ler: str = ""
    new_ler: list = []
    if args != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        x = sys.argv[1]
        try:
            print(f"Accessing file: '{x}'")
            file = open(x, "r")
        except (OSError) as error:
            print(f"Error opening file '{x}':", error)
            return
        try:
            print("---")
            ler = file.read()
            print(ler)
            print("---")
        except (OSError) as error:
            print(f"Error reading file '{x}':", error)
            return
        finally:
            file.close()
            print(f"File '{x}' is closed.")
    new_ler = [line + "#" for line in ler.splitlines()]
    print("\nTransform data:")
    print("---")
    for y in new_ler:
        print(y)
    print("---")
    phrase: str = "Enter new file name (or empty): "
    input1 = input(phrase)
    if input1 != "":
        try:
            new_file = open(f"{input1}", "w")
            print(f"Saving data to '{input1}'")
        except OSError as error:
            print(f"Error opening file '{input1}':", error)
            return
        for z in new_ler:
            try:
                new_file.write(z + "\n")
            except OSError as error:
                print(f"Error writing file '{input1}':", error)
                new_file.close()
                return
        new_file.close()
        print(f"Data saved in file '{input1}'")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
