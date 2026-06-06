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
            print("---")
            ler = file.read()
            print(ler)
            print("---")
            file.close()
            print(f"File '{x}' is closed.")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error opening file '{x}':", error)
    new_ler = [line + "#" for line in ler.splitlines()]
    print("\nTransform data:")
    print("---")
    for y in new_ler:
        print(y)
    print("---")
    phrase: str = "Enter new file name (or empty): "
    try:
        sys.stdout.write(phrase)
    except OSError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{input1}':", error)
    finally:
        sys.stdout.flush()
    input1 = sys.stdin.readline().rstrip('\n')
    if input1 != "":
        try:
            new_file = open(f"{input1}", "w")
            print(f"Saving data to '{input1}'")
            for z in new_ler:
                new_file.write(z + "\n")
            new_file.close()
        except (OSError) as error:
            sys.stderr.write(f"[STDERR] Error opening file '{input1}':", error)
        print(f"Data saved in file '{input1}'")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
