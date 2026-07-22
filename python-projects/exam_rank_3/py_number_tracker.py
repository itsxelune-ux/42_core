def pattern_tracker(text: str) -> int:
    count = 0
    nbrs = "0123456789"

    for i in range(0, len(text) - 1, 1):
        if text[i] in nbrs:
            if text[i + 1] in nbrs:
                if int(text[i]) < int(text[i + 1]):
                    count += 1

    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
