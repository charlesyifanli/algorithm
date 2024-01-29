from typing import List


class Solution(object):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [8, 1, 2, 2, 3]
        assert Solution().smallerNumbersThanCurrent(nums) == [4, 0, 1, 1, 3]

        print('Succeed')


    test()
