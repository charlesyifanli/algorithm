from typing import List


class Solution(object):
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -x)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])


if __name__ == '__main__':
    def test():
        # case
        nums = [1, 2, 3, 4]
        assert Solution().maximumProduct(nums) == 24

        print('Succeed')


    test()
