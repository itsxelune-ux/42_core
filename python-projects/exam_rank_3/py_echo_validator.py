def echo_validator(text: str) -> bool:
    return text == text[::-1]


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("race a car"))
