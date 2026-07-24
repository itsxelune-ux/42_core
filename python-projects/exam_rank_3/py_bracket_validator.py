# def bracket_validator(s: str) -> bool:
#     stack = []
#     pairs = {
#         ")": "(",
#         "}": "{",
#         "]": "["
#     }

#     for ch in s:
#         if ch in "({[":
#             stack.append(ch)
#         else:
#             if not stack:
#                 return False

#             last = stack.pop()
#             if last != pairs[ch]:
#                 return False

#     return not stack


# if __name__ == "__main__":
#     print(bracket_validator("()"))
#     print(bracket_validator("({})"))
#     print(bracket_validator("([)"))
def bracket_validator(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False

            last = stack.pop()
            if last != pairs[ch]:
                return False

    return not stack


if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
