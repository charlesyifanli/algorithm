from typing import List


class Solution(object):
    def findFinalValue(self, nums: List[int], original: int) -> int:
        res = 0
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [5, 3, 6, 1, 12]
        original = 3
        assert Solution().findFinalValue(nums, original) == 24

        # case
        nums = [2, 7, 9]
        original = 4
        assert Solution().findFinalValue(nums, original) == 4

        print('Succeed')


    test()
