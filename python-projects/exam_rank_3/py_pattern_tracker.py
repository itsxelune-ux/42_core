def pattern_tracker(text: str) -> int:
    count = 0
    numbers = "0123456789"

    for i in range(0, len(text) - 1, 1):
        if text[i] in numbers:
            if text[i + 1] in numbers:
                if int(text[i]) < int(text[i + 1]):
                    count += 1
    return count


if __name__ == "__main__": 
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
