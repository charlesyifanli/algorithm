def get_ord(char: str) -> int:
    return ord(char) - ord('a') + 1


def f(s: str) -> int:
    dp = [[0, 0] for _ in range(len(s))]
    dp[0][1] = get_ord(s[0])

    for i in range(1, len(s)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + get_ord(s[i])

    return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    print(f(input()))
