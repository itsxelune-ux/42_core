#!/usr/bin/env python3

print("=== Garden Plant Health Checker ===")
print()


def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 6)
        print(result)
    except ValueError as e:
        print("Error:", e)

    print()
    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 6)
        print(result)
    except ValueError as e:
        print("Error:", e)

    print()
    print("Testing bad water level...")
    try:
        result = check_plant_health("tomato", 15, 6)
        print(result)
    except ValueError as e:
        print("Error:", e)

    print()
    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as e:
        print("Error:", e)

    print()
    print("All error raising tests completed!")


test_plant_checks()
