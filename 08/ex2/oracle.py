from sys import prefix, base_prefix


def main() -> None:
    is_venv = prefix != base_prefix
    if is_venv:
        print("\nORACLE STATUS: Reading the Matrix...")
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
