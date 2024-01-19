from typing import List


class Solution(object):
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_ = len(matrix)
        dp = [[0] * len_ for _ in range(len_)]
        for i in range(len_):
            dp[0][i] = matrix[0][i]
        for i in range(1, len_):
            for j in range(len_):
                dp[i][j] = matrix[i - 1][j]
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == len_ - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1]) + matrix[i][j]
        return min(dp[- 1])


'''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        # dp[0][j] = matrix[0][j]
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]

        return min(dp[-1])
'''
if __name__ == '__main__':
    def test():
        # case
        matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
        assert Solution().minFallingPathSum(matrix) == 13

        # case
        matrix = [[-19, 57], [-40, -5]]
        assert Solution().minFallingPathSum(matrix) == -59

        print('Succeed')


    test()
