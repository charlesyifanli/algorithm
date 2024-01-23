from typing import List
from collections import Counter


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = dict(Counter(nums))
        for key, val in dict_.items():
            if val > len(nums) // 2: return key
        return -1


if __name__ == '__main__':
    def test():
        # case
        nums = [2, 2, 1, 1, 1, 2, 2]
        assert Solution().majorityElement(nums) == 2

        print('Succeed')


    test()
