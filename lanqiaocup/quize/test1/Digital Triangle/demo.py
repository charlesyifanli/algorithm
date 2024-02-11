class Solution(object):
    def function(self) -> None:
        n = int(input())
        ls, dp = [], [[0 for j in range(i + 1)] for i in range(n)]
        for i in range(n):
            curr = [int(x) for x in input().split()]
            ls.append(curr)
        for i in range(n):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    dp[i][j] = ls[i][j]
                elif j == 0:
                    dp[i][j] = ls[i][j] + dp[i - 1][j]
                elif j == i:
                    dp[i][j] = ls[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = ls[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
        if n % 2 == 0:
            print(max(dp[n - 1][(n - 1) // 2], dp[n - 1][(n - 1) // 2 + 1]))
        else:
            print(dp[n - 1][(n - 1) // 2])


Solution().function()
