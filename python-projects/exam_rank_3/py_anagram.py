def anagram(s1: str, s2: str) -> bool:
    return (sorted(s1) == sorted(s2))


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("hello", "world"))
