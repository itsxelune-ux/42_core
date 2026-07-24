def string_sculptor(text: str) -> str:
    res = ""
    flag = True

    for i in range(len(text)):
        if text[i] == " ":
            res += text[i]
            flag = True

        elif text[i].isalpha() and flag:
            res += text[i].lower()
            flag = False

        elif text[i].isalpha() and not flag:
            res += text[i].upper()
            flag = True

        else:
            res += text[i]

    return res


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
