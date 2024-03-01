def get_2d_pref(arr: list) -> list:
    pref = [[0 for _ in range(len(arr[0]) + 1)] for _ in range(len(arr) + 1)]
    pref[0][0] = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 and j == 0: continue
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + arr[i][j]
    return pref


def get_2d_diff(arr: list) -> list:
    if not arr or not arr[0]:
        return []
    rows, cols = len(arr), len(arr[0])
    diff = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                diff[i][j] = arr[i][j]
            elif i == 0:
                diff[i][j] = arr[i][j] - arr[i][j - 1]
            elif j == 0:
                diff[i][j] = arr[i][j] - arr[i - 1][j]
            else:
                diff[i][j] = arr[i][j] - arr[i - 1][j] - arr[i][j - 1] + arr[i - 1][j - 1]
    return diff


def get_2d_sum(arr: list, x1: int, y1: int, x2: int, y2: int) -> int:
    pref = get_2d_pref(arr)
    print(pref)
    return pref[x2][y2] - pref[x2][y1 - 1] - pref[x1 - 1][y2] + pref[x1 - 1][y1 - 1]


arr = [[1, 2], [2, 3], [3, 4]]

print(get_2d_sum(arr, 1, 1, 2, 1))