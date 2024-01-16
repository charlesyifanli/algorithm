from typing import List


class Solution(object):
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return nums[0] * nums[1] - nums[-2] * nums[-1]


if __name__ == '__main__':
    def test():
        # case
        nums = [5, 6, 2, 7, 4]
        assert Solution().maxProductDifference(nums) == 34

        # case
        nums = [4, 2, 5, 9, 7, 4, 8]
        assert Solution().maxProductDifference(nums) == 64

        print('Succeed')


    test()
