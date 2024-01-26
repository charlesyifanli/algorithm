from typing import List


class Solution(object):
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[0:len(nums):2])


if __name__ == '__main__':
    def test():
        # case
        nums = [6, 2, 6, 5, 1, 2]
        assert Solution().arrayPairSum(nums) == 9

        print('Succeed')


    test()
