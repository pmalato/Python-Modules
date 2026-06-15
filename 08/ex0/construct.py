from sys import prefix, base_prefix, executable
from os import path
import site


def main() -> None:
    is_venv = prefix != base_prefix
    if is_venv:
        print("MATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python: ", executable)
        print("Virtual Environment: ", path.basename(prefix))
        print("Environmental Path: ", path.abspath(prefix))
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("without global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python: ", {executable})
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
