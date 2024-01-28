from typing import List


class Solution(object):
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        res = 0
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [4, 2, 3]
        k = 1
        assert Solution().largestSumAfterKNegations(nums, k) == 5

        print('Succeed')


    test()
