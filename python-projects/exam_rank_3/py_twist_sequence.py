def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0:
        return arr

    k = k % len(arr)
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))