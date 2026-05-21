def ft_water_reminder():
    user = int(input("Days since last watering: "))
    if user > 2:
        print("Water the plants!")
    else:
        print("Plants are fine!")
