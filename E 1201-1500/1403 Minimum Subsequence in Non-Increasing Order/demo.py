from typing import List


class Solution(object):
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        nums.sort(reverse=True)
        for i in range(1, len(nums)+1):
            if i == len(nums): return nums
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]


if __name__ == '__main__':
    def test():
        nums = [4, 3, 10, 9, 8]
        assert Solution().minSubsequence(nums) == [10, 9]

        nums = [6]
        assert Solution().minSubsequence(nums) == [6]

        print('Succeed')


    test()
