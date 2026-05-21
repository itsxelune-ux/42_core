
def ft_count_harvest_iterative():
    user = int(input("Days until harvest: "))
    for day in range(1, user + 1):
        print("Day", day)
    print("Harvest time!")
