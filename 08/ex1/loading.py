from sys import prefix, base_prefix
import importlib as imp
from importlib.metadata import PackageNotFoundError


def check_modules(name: str, description: str) -> str | None:
    try:
        imp.import_module(name)
    except ImportError:
        return None
    try:
        version = imp.metadata.version(name)
        return f"[OK] {name} ({version}) - {description} ready"
    except PackageNotFoundError:
        return None


def main() -> None:

    is_venv = prefix != base_prefix
    if (is_venv):
        print("\nLOADING STATUS: Loading programs...\n")
        print("Checking dependencies...")
        imp_error1 = check_modules("pandas", "Data manipulation")
        imp_error2 = check_modules("numpy", "Numeric computation")
        imp_error3 = check_modules("matplotlib", "Visualization")
        if imp_error1 is not None:
            print("[MISSING] pandas - Data manipulation unachieved")
        else:
            print(imp_error1)
        if imp_error2 is not None:
            print("[MISSING] numpy - Numeric computation unachieved")
        else:
            print(imp_error2)
        if imp_error3 is not None:
            print("[MISSING] matplotlib - Visualization unachieved")
        else:
            print(imp_error3)
        if imp_error1 is not None or imp_error2 is not None or imp_error3 is not None:
            return
        print("Analyzing Matrix data...")
        try:
            import pandas as pd  # type: ignore
            # missing application
        except ImportError as error:
            print("Import error: ", error)
        print("Processing 1000 data points...")
        try:
            import numpy as np  # type: ignore
            # missing application
        except ImportError as error:
            print("Import error: ", error)
        print("Generating visualization...")
        try:
            import matplotlib.pyplot as plt  # type: ignore
            # missing application
        except ImportError as error:
            print("Import error: ", error)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
