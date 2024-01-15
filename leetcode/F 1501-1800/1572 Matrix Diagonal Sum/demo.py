from typing import List


class Solution(object):
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0
        for i, val in enumerate(mat): sum_ += val[i] + val[len(mat) - 1 - i]
        return sum_ if len(mat) % 2 == 0 else sum_ - mat[len(mat) // 2][len(mat) // 2]


if __name__ == '__main__':
    def test_diagonal_sum():
        # case
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        assert Solution().diagonalSum(matrix) == 25

        # case
        matrix = [[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]]
        assert Solution().diagonalSum(matrix) == 8

        print('Succeed')


    test_diagonal_sum()
