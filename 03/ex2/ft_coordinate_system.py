import math


def get_player_position() -> None:
    phrase: str = "Enter new coordinates as floats in format 'x, y, z': "
    coordinates: list
    while True:
        try:
            temp: str = ""
            coordinates = []
            for x in input(phrase):
                if x == " ":
                    continue
                elif x == ",":
                    coordinates += [float(temp)]
                    temp = ""
                else:
                    temp += x
            coordinates += [float(temp)]
            coordinates = [tuple(coordinates)]
            break
        except ValueError:
            print("Invalid syntax")


def main() -> None:
    print("Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    get_player_position()
    print("done")


if __name__ == "__main__":
    main()
