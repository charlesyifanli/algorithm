class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])


if __name__ == '__main__':
    assert Solution().minimumTotal(
        triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    ) == 11

    assert Solution().minimumTotal(
        triangle=[[-10]]
    ) == -10
