def anagram(s1: str, s2: str) -> bool:
    return sorted(s1.replace(" ", "").lower()) \
        == sorted(s2.replace(" ", "").lower())


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))