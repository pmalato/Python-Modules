from sys import prefix, base_prefix
import importlib as imp
from importlib.metadata import PackageNotFoundError


def check_modules(name: str) -> str | None:
    try:
        module = imp.import_module(name)
    except ImportError:
        return None
    try:
        version = imp.metadata()
        return f"{module}, {version}, 'unknown'"
    except PackageNotFoundError:
        return None


def main() -> None:

    is_venv = prefix != base_prefix
    if (is_venv):
        imp_error1 = check_modules("pandas")
        imp_error2 = check_modules("numpy")
        imp_error3 = check_modules("matplotlib")
        if imp_error1:
            print(imp_error1)
        if imp_error2:
            print(imp_error2)
        if imp_error3:
            print(imp_error3)
        if imp_error1 | imp_error2 | imp_error3:
            return
        import pandas as pd  # type: ignore
        import numpy as np  # type: ignore
        import matplotlib.pyplot as plt  # type: ignore
        df = pd.DataFrame()
        df["Nation"] = [
            "Earth Realm",
            "Air Nomads",
            "Fire Nation",
            "Water Poles"]
        df["Quantity"] = [50, 70, 30, 90]
        df["Bender"] = [30, 13, 15, 65]
        df["Non-bender Integration"] = [True, True, False, False]
        print("\nLOADING STATUS: Loading programs...")

    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
