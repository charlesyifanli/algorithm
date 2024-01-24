from typing import List
from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_ = dict(Counter(nums))
        if len(nums) != len(dict_.items()):
            return True
        return False


if __name__ == '__main__':
    def test():
        # case
        nums = [1, 2, 3, 1]
        assert Solution().containsDuplicate(nums) == True
        print('Succeed')


    test()
