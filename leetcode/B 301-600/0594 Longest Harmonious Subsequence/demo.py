from typing import List
from collections import Counter


class Solution(object):
    def findLHS(self, nums: List[int]) -> int:
        dict_ = Counter(nums)
        res = 0
        for val in dict_:
            if val + 1 in dict_:
                res = max(res, dict_[val] + dict_[val + 1])
        return res


if __name__ == '__main__':
    def test():
        # case
        print('Succeed')


    test()
