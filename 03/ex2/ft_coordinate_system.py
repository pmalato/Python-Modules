import math


def get_player_position() -> tuple:
    phrase: str = "Enter new input1 as format in 'x, y, z': "
    input1: list
    temp: str
    count: int = 0
    distance: float
    while True:
        try:
            temp = ""
            input1 = []
            count = 0
            for x in input(phrase):
                if x == " ":
                    temp = ""
                    continue
                elif x == ",":
                    input1 += [float(temp)]
                    count += 1
                    temp = ""
                else:
                    temp += x
            input1 += [float(temp)]
            count += 1
            if count != 3:
                raise ValueError
            coordinates: tuple = tuple(input1)
            break
        except ValueError:
            print("Invalid syntax")
    print(f"Tuple gathered: {input1}")
    print(f"It includes: X = {input1[0]},"
          f" Y = {input1[1]}, Z = {input1[2]}")
    distance = math.sqrt(
        (input1[0] - 0.0)**2 +
        (input1[1] - 0.0)**2 +
        (input1[0] - 0.0)**2
        )
    print(f"Distance to center: {distance}")
    return coordinates


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    get_player_position()
    print("done")


if __name__ == "__main__":
    main()
