import pandas as pd  # type: ignore
import numpy as np
import matplotlib.pyplot as plt
from sys import prefix, base_prefix
import importlib


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
        print("")
        print("")
        plt.show()
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
