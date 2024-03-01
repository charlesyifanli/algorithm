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


def regional_2d_sum(arr: list, top_left: list[int], bottom_right: list[int]) -> int:
    x1, y1 = top_left
    x2, y2 = bottom_right
    pref = get_2d_pref(arr)
    return pref[x2][y2] - pref[x2][y1 - 1] - pref[x1 - 1][y2] + pref[x1 - 1][y1 - 1]


def regional_2d_add_minus(arr: list, top_left: list[int], bottom_right: list[int], num: int) -> list:
    rows, cols = len(arr), len(arr[0])

    # 获取差分数组
    diff = get_2d_diff(arr)

    # 确定要修改的区域
    row_start, col_start = top_left
    row_end, col_end = bottom_right

    # 更新差分数组以实现加减操作
    diff[row_start][col_start] += num
    if row_end + 1 < rows:
        diff[row_end + 1][col_start] -= num
    if col_end + 1 < cols:
        diff[row_start][col_end + 1] -= num
    if row_end + 1 < rows and col_end + 1 < cols:
        diff[row_end + 1][col_end + 1] += num

    # 从差分数组构建原始二维数组
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                arr[i][j] = diff[i][j]
            elif i == 0:
                arr[i][j] = diff[i][j] + arr[i][j - 1]
            elif j == 0:
                arr[i][j] = diff[i][j] + arr[i - 1][j]
            else:
                arr[i][j] = diff[i][j] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    return arr


arr = [[1, 2], [2, 3], [3, 4]]

print(regional_2d_add_minus(arr, [2, 1], [2, 1], 1))
