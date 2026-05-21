#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_plant(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":

    rose = Plant("Rose", 25, 30)

    start_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(6):
        rose.grow()
        rose.age_plant()

    print("=== Day 7 ===")
    print(rose.get_info())

    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
