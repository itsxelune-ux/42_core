def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        if not (2 <= from_base <= 36 or 2 <= to_base <= 36):
            raise ValueError("Error")

        num = int(number, from_base)
        if num == 0:
            return "0"
        result = ""

        while num:
            result += letters[num % to_base]
            num //= to_base

        return result[::-1]
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
