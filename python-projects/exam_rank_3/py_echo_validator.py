def echo_validator(text: str) -> bool:
    clean = ""

    for ch in text:
        if ch.isalnum():
            clean += ch.lower()

    return clean == clean[::-1]


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))