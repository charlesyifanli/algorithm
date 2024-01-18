from typing import List


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res ^= val
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [2, 2, 1]
        assert Solution().singleNumber(nums) == 1

        # case
        nums = [4, 1, 2, 1, 2]
        assert Solution().singleNumber(nums) == 4

        print('Success')


    test()
