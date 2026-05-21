#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, value):
        if value >= 0:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print()
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value):
        if value >= 0:
            self.__age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")


if __name__ == "__main__":

    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 25, 30)

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)

    print()
    print(
        f"Current plant: {rose.name} "
        f"({rose.get_height()}cm, {rose.get_age()} days)"
    )
