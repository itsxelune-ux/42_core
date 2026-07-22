def number_base_converter(number: str, from_base: int, to_base: int):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if not (2 <= from_base <= 36 or 2 <= to_base <= 36):
            raise ValueError('ERROR')

        num = int(number, from_base)
        if num == 0:
            return "0"
        res = ""
        while num:
            res += digits[num % to_base]
            num //= to_base
        return res[::-1]
    except ValueError as e:
        print(f'ERROR: {e}')


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
