def get_final_board(n, ope):
    diff = [[0] * (n + 1) for _ in range(n + 1)]

    for operation in ope:
        x1, y1, x2, y2 = operation
        diff[x1][y1] += 1
        if x2 + 1 <= n:
            diff[x2 + 1][y1] -= 1
        if y2 + 1 <= n:
            diff[x1][y2 + 1] -= 1
        if x2 + 1 <= n and y2 + 1 <= n:
            diff[x2 + 1][y2 + 1] += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]

    chess = [[0] * n for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            chess[i - 1][j - 1] = 1 if diff[i][j] % 2 != 0 else 0

    return chess


if __name__ == '__main__':
    n, m = map(int, input().split())
    ope_ls = [list(map(int, input().split())) for _ in range(m)]

    final_board = get_final_board(n, ope_ls)
    for row in final_board:
        print("".join(map(str, row)))

# Time Exceeded ! ! !
#
# def f(chess_ls: list, ope_ls: list) -> list:
#     for ope in ope_ls:
#         x1, y1, x2, y2 = ope
#         for x_idx in range(x1, x2 + 1):
#             for y_idx in range(y1, y2 + 1):
#                 chess_ls[x_idx][y_idx] += 1
#                 chess_ls[x_idx][y_idx] = 0 if chess_ls[x_idx][y_idx] % 2 == 0 else 1
#     return chess_ls
#
#
# n, m = list(map(int, input().split()))
#
# chess_ls = [[0 for _ in range(n)] for _ in range(n)]
#
# ope_ls = []
# for i in range(m):
#     curr = list(map(int, input().split()))
#     curr = [x - 1 for x in curr]
#     ope_ls.append(curr)
#
# chess_ls = f(chess_ls, ope_ls)
# for item in chess_ls:
#     s = ''.join(str(x) for x in item)
#     print(s)
