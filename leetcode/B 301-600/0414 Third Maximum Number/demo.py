from typing import List


class Solution(object):
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3: return max(nums)
        nums.sort(reverse=True)
        return nums[2]


if __name__ == '__main__':
    def test():
        # case
        nums = [2, 2, 3, 1]
        assert Solution().thirdMax(nums) == 1

        # case
        nums = [1, 1, 2]
        assert Solution().thirdMax(nums) == 2

        print('Succeed')


    test()
