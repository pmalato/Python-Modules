def ft_count_harvest_iterative() -> None:
    time = int(input("Days until harvest: "))
    while time > 0:
        print("Day", time)
        time -= 1
    print("Harvest time!")
