from typing import List


def no_carry_borrow(num0: int, num1: int) -> int:
    return abs(num0 - num1)


def carry(num0: int, num1: int) -> int:
    return abs(10 - num0 + num1)


def borrow(num0: int, num1: int) -> int:
    return abs(10 - num1 + num0)


def str2list(s0: str, s1: str, len_: int) -> list[list]:
    ls_0, ls_1 = [], []
    for i in range(len_):
        ls_0.append(int(s0[i]))
        ls_1.append(int(s1[i]))
    return [ls_0, ls_1]


def f(len_: int, s0: str, s1: str) -> int:
    ls_0, ls_1 = str2list(s0, s1, len_)

    dp = [[0, 0, 0] for _ in range(len_)]

    dp[0][0] = no_carry_borrow(ls_0[0], ls_1[0])
    dp[0][1] = carry(ls_0[0], ls_1[0])
    dp[0][2] = borrow(ls_0[0], ls_1[0])

    for i in range(1, len_):
        dp[i][0] = min(dp[i - 1][0] + no_carry_borrow(ls_0[i], ls_1[i]),
                       dp[i - 1][1] + no_carry_borrow(ls_0[i] + 1, ls_1[i]),
                       dp[i - 1][2] + no_carry_borrow(ls_0[i] - 1, ls_1[i]))
        dp[i][1] = min(dp[i - 1][0] + carry(ls_0[i], ls_1[i]),
                       dp[i - 1][1] + carry(ls_0[i] + 1, ls_1[i]),
                       dp[i - 1][2] + carry(ls_0[i] - 1, ls_1[i]))
        dp[i][2] = min(dp[i - 1][0] + borrow(ls_0[i], ls_1[i]),
                       dp[i - 1][1] + borrow(ls_0[i] + 1, ls_1[i]),
                       dp[i - 1][2] + borrow(ls_0[i] - 1, ls_1[i]))

    return min(dp[-1])


n = int(input())
x = input()[::-1]
y = input()[::-1]

print(f(n, x, y))
