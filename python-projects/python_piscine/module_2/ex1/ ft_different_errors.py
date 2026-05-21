#!/usr/bin/env python3

def garden_operations():

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)

    print()

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print()

    try:
        print("Testing FileNotFoundError...")
        f = open("missing.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print()

    try:
        print("Testing KeyError...")
        d = {"apple": 5}
        d["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e)

    print()

    try:
        print("Testing multiple errors together...")
        int("oops")
        5 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print()


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()

    garden_operations()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
