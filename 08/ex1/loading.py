import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from sys import prefix, base_prefix
import importlib as imp
from importlib.metadata import PackageNotFoundError


def check_modules(name: str) -> str | None:
    try:
        module = imp.import_module(name)
    except ImportError:
        return None
    try:
        version = module.metadata
        return f"{module}, {version}, 'unknown'"
    except PackageNotFoundError:
        return None


def main() -> None:
    is_venv = prefix != base_prefix
    if (is_venv):
        df = pd.DataFrame()
        ar1 = np.array([3, 10])
        ar2 = np.array([5, 7])
        plt.plot(ar1, ar2)
        df["Nation"] = [
            "Earth Realm",
            "Air Nomads",
            "Fire Nation",
            "Water Poles"]
        df["Quantity"] = [50, 70, 30, 90]
        df["Bender"] = [30, 13, 15, 65]
        df["Non-bender Integration"] = [True, True, False, False]
        print("\nLOADING STATUS: Loading programs...")
        print("")
        print("")
        plt.show()
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
