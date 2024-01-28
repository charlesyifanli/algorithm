from typing import List


class Solution(object):
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])


if __name__ == '__main__':
    def test():
        # case
        nums = [-7, -3, 2, 3, 11]
        assert Solution().sortedSquares(nums) == [4, 9, 9, 49, 121]

        print('Succeed')


    test()
