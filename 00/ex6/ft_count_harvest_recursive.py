def ft_count_harvest_recursive() -> None:
    time = int(input("Days until harvest: "))

    def recursion_count(time):
        if time == 0:
            print("Harvest time!")
        else:
            print("Day", time)
            recursion_count(time - 1)
    recursion_count(time)
