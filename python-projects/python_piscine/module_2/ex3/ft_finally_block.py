#!/usr/bin/env python3

print("=== Garden Watering System ===")
print()


def water_plants(plant_list):
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print("Watering", plant)

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering complited successfully!")

    print("\nTesting with error...")
    plants = ["tomato", None, "carrots"]
    water_plants(plants)
    print()
    print("Cleanup always happens, even with errors!")


test_watering_system()
