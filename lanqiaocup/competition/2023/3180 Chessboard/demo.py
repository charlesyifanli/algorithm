def f(chess_ls: list, ope_ls: list) -> list:
    for ope in ope_ls:
        x1, y1, x2, y2 = ope
        for x_idx in range(x1, x2 + 1):
            for y_idx in range(y1, y2 + 1):
                chess_ls[x_idx][y_idx] += 1
                chess_ls[x_idx][y_idx] = 0 if chess_ls[x_idx][y_idx] % 2 == 0 else 1
    return chess_ls


n, m = list(map(int, input().split()))

chess_ls = [[0 for _ in range(n)] for _ in range(n)]

ope_ls = []
for i in range(m):
    curr = list(map(int, input().split()))
    curr = [x - 1 for x in curr]
    ope_ls.append(curr)

chess_ls = f(chess_ls, ope_ls)
for item in chess_ls:
    s = ''.join(str(x) for x in item)
    print(s)
