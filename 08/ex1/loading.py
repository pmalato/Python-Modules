from sys import prefix, base_prefix
import importlib as imp
from importlib.metadata import PackageNotFoundError


def check_modules(name: str, description: str) -> str | None:
    try:
        imp.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - {description} unachieved")
        return None
    try:
        version = imp.metadata.version(name)
        return f"[OK] {name} ({version}) - {description} ready"
    except PackageNotFoundError:
        print(f"[OK] {name} [MISSING] version - {description} unachieved")
        return None


def main() -> None:

    is_venv = prefix != base_prefix
    if (is_venv):
        print("\nLOADING STATUS: Loading programs...\n")
        print("Checking dependencies...")
        imp_error1 = check_modules("pandas", "Data manipulation")
        imp_error2 = check_modules("numpy", "Numeric computation")
        imp_error3 = check_modules("matplotlib", "Visualization")
        png_reference = "matrix_analysis.png"
        if imp_error1 is None or imp_error2 is None or imp_error3 is None:
            return
        else:
            print(imp_error1)
            print(imp_error2)
            print(imp_error3)
        print("\nAnalyzing Matrix data...")
        try:
            import numpy as np  # type: ignore
            arr = np.random.randint(0, 10, (20, 50), int)
        except ImportError as error:
            print("Import error: ", error)
            return None
        print("Processing 1000 data points...")
        try:
            import pandas as pd  # type: ignore
            df = pd.DataFrame(arr)
            change = pd.DataFrame.stack(df)
            change.value_counts()
        except Exception as error:
            print("Error: ", error)
            return None
        print("Generating visualization...")
        try:
            from matplotlib.colors import (  # type: ignore
                LinearSegmentedColormap as mcl)  # type: ignore
            green_matrix_cmap = mcl('green_matrix', {
                'red': [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
                'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)],
                'blue': [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)]
            })
        except Exception as error:
            print("Error: ", error)
        try:
            import matplotlib.pyplot as plt  # type: ignore
            plt.imshow(
                df, cmap=green_matrix_cmap, interpolation='nearest')
            plt.colorbar()
        except Exception as error:
            print("Error: ", error)
            return None
        print("\nAnalysis complete!")
        try:
            plt.savefig(png_reference)
        except Exception:
            print(f"Unable to save to: {png_reference}")
            return None
        print(f"Results saved to: {png_reference}")
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
