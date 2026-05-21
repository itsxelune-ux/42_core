#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = int(self.height * 0.156)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":

    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 450, 1500, 40),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "autumn", "vitamin A"),
    ]

    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.height}cm, "
            f"{flower.age} days, {flower.color} color"
        )
        flower.bloom()
        print()

    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, "
            f"{tree.trunk_diameter}cm diameter"
        )
        tree.produce_shade()
        print()

    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.height}cm, "
            f"{vegetable.age} days, {vegetable.harvest_season} harvest"
        )
        vegetable.show_nutrition()
        print()
