from typing import List


class Solution(object):
    def missingNumber(self, nums: List[int]) -> int:
        for val in range(len(nums) + 1):
            if val not in nums:
                return val


if __name__ == '__main__':
    def test():
        # case
        nums = [3, 0, 1]
        assert Solution().missingNumber(nums) == 2

        # case
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        assert Solution().missingNumber(nums) == 8

        print('Success')


    test()
