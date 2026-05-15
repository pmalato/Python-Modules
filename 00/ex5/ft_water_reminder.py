def ft_water_reminder() -> None:
    refresh = int(input("Days since last watering: "))
    if refresh > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
