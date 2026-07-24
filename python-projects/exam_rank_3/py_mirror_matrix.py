def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = []

    for row in matrix:
        result.append(row[::-1])

    return result


if __name__ == "__main__":
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))