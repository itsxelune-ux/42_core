def vowels_count(s: str) -> int:
    count = 0
    vowels = "aeiouAEIOU"

    for ch in s:
        if ch in vowels:
            count += 1
    return count


def should_swap(a: str, b: str) -> bool:
    if len(a) != len(b):
        return len(a) > len(b)
    if a.lower() != b.lower():
        return a.lower() > b.lower()
    if vowels_count(a) != vowels_count(b):
        return vowels_count(a) > vowels_count(b)
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
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
