from typing import List


class Solution(object):
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1: return [i, i + 1]


if __name__ == '__main__':
    def test():
        # case
        nums = [1, 2, 2, 4]
        assert Solution().findErrorNums(nums) == [2, 3]

        print('Succeed')


    test()
