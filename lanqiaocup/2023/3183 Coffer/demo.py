def f(len_: int, old_val: str, new_val: str) -> int:
    dp = [[0, 0, 0] for _ in range(len_)]

    dp[0][0] = no_carry_borrow(int(old_val[0]), int(new_val[0]))
    dp[0][1] = carry(int(old_val[0]), int(new_val[0]))
    dp[0][2] = borrow(int(old_val[0]), int(new_val[0]))

    for i in range(1, len_):
        dp[i][0] = min(dp[i - 1][0] + no_carry_borrow(int(old_val[i]), int(new_val[i])),
                       dp[i - 1][1] + no_carry_borrow(int(old_val[i]) + 1, int(new_val[i])),
                       dp[i - 1][2] + no_carry_borrow(int(old_val[i]) - 1, int(new_val[i])))
        dp[i][1] = min(dp[i - 1][0] + carry(int(old_val[i]), int(new_val[i])),
                       dp[i - 1][1] + carry(int(old_val[i]) + 1, int(new_val[i])),
                       dp[i - 1][2] + carry(int(old_val[i]) - 1, int(new_val[i])))
        dp[i][2] = min(dp[i - 1][0] + borrow(int(old_val[i]), int(new_val[i])),
                       dp[i - 1][1] + borrow(int(old_val[i]) + 1, int(new_val[i])),
                       dp[i - 1][2] + borrow(int(old_val[i]) - 1, int(new_val[i])))

    return min(dp[-1])


def no_carry_borrow(num0: int, num1: int) -> int:
    return abs(num0 - num1)


def carry(num0: int, num1: int) -> int:
    return abs(10 - num0 + num1)


def borrow(num0: int, num1: int) -> int:
    return abs(10 - num1 + num0)


n = int(input())
x = input()[::-1]
y = input()[::-1]

print(f(n, x, y))
