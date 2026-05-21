def ft_plant_age():
    user = int(input("Enter plant age in days:"))
    if user > 60:
        print("Plant ready to harvest!")
    else:
        print("Plant needs more time to grow.")
