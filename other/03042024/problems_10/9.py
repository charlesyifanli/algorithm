def top_left(arr: list, row: int, column: int) -> int:
    res = 0
    num = arr[row][column]
    row -= 1
    column -= 1
    while (row >= 0 and column >= 0) and arr[row][column] == num:
        res += 1
        row -= 1
        column -= 1
    return res


def top_right(arr: list, row: int, column: int) -> int:
    res = 0
    num = arr[row][column]
    row -= 1
    column += 1
    while (row >= 0 and column < len(arr[0])) and arr[row][column] == num:
        res += 1
        row -= 1
        column += 1
    return res


def down(arr: list, row: int, column: int) -> int:
    res = 0
    num = arr[row][column]
    row += 1
    while row < len(arr) and arr[row][column] == num:
        res += 1
        row += 1
    return res


def f(arr: list) -> int:
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            len_ = min(top_left(arr, i, j), top_right(arr, i, j), down(arr, i, j))
            res = len_ if len_ > res else res
    return res


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    arr = []
    for i in range(n):
        arr.append(''.join(input().split()))
    print(f(arr))
