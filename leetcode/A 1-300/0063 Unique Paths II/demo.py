class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    assert Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
