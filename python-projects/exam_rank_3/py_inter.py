def inter(s1: str, s2: str) -> str:
    result = ""

    for ch in s1:
        for nz in s2:
            if ch == nz and ch not in result:
                result += ch
    return result


if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))