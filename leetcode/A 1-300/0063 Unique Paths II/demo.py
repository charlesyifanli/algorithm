class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = 1 - obstacleGrid[0][0]
#
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     if i > 0:
#                         dp[i][j] += dp[i - 1][j]
#                     if j > 0:
#                         dp[i][j] += dp[i][j - 1]
#
#         return dp[-1][-1]


if __name__ == '__main__':
    assert Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
