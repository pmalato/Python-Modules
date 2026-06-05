import math


def get_player_position() -> tuple:
    phrase: str = "Enter new input1 as format in 'x, y, z': "
    input1: list
    temp: str
    count: int = 0
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
    return coordinates


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coord1: tuple = get_player_position()
    print(f"It includes: X = {coord1[0]},"
          f" Y = {coord1[1]}, Z = {coord1[2]}")
    print(f"Tuple gathered: {coord1}")
    distance1: float = math.sqrt(
        (coord1[0] - 0.0)**2 +
        (coord1[1] - 0.0)**2 +
        (coord1[2] - 0.0)**2)
    print(f"Distance to center: {round(distance1, 4)}")
    print("\nGet a second set of coordinates")
    coord2: tuple = get_player_position()
    distance2: float = math.sqrt(
        (coord2[0] - coord1[0])**2 +
        (coord2[1] - coord1[1])**2 +
        (coord2[2] - coord1[2])**2)
    print(f"Distance betewen the 2 sets of coordinates: {round(distance2, 4)}")


if __name__ == "__main__":
    main()
