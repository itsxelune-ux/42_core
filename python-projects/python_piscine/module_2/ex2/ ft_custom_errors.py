#!/usr/bin/env python3

print("=== Custom Garden Errors Demo ===")
print()


class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


print("Testing PlantError...")
try:
    check_plant()
except PlantError as e:
    print("Caught PlantError:", e)
    print()


print("Testing WaterError...")
try:
    check_water()
except WaterError as e:
    print("Caught WaterError:", e)
    print()


print("Testing catching all garden errors...")

try:
    check_plant()
except GardenError as e:
    print("Caught a garden error:", e)

try:
    check_water()
except GardenError as e:
    print("Caught a garden error:", e)
    print()


print("All custom error types work correctly!")
