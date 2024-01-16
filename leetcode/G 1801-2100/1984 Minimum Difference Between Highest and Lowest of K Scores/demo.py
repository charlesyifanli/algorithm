from typing import List


class Solution(object):
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


if __name__ == '__main__':
    def test():
        # case
        nums = [90]
        k = 1
        assert Solution().minimumDifference(nums, k) == 0

        # case
        nums = [9, 4, 1, 7]
        k = 2
        assert Solution().minimumDifference(nums, k) == 2

        print('Succeed')


    test()
