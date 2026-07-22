def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1
    return count


def should_swap(a: str, b: str) -> bool:
    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False

    if a.lower() > b.lower():
        return True
    if a.lower() < b.lower():
        return False

    if count_vowels(a) > count_vowels(b):
        return True
    if count_vowels(a) < count_vowels(b):
        return False

    return False


def cryptic_sorter(strings: list[str]) -> list[str]:
    result = strings[:]

    n = len(result)
    for i in range(n):
        for j in range(n - 1 - i):
            if should_swap(result[j], result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    print(cryptic_sorter(["apple", "cat", "bananna", "dog", "elephant"]))
