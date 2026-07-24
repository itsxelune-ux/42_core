def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for ch in text:
        if ch in lower:
            index = lower.index(ch)
            result += lower[(index + shift) % 26]

        elif ch in upper:
            index = upper.index(ch)
            result += upper[(index + shift) % 26]

        else:
            result += ch

    return result


print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
