from typing import List
from collections import Counter


class Solution(object):
    def countElements(self, nums: List[int]) -> int:
        res = 0
        sorted_list = sorted(list(dict(Counter(nums)).items()), key=lambda x: x[0])
        for i in range(1, len(sorted_list) - 1):
            res += sorted_list[i][1]
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [-3, 3, 3, 90]
        assert Solution().countElements(nums) == 2

        # case
        nums = [11, 7, 2, 15]
        assert Solution().countElements(nums) == 2

        print('Succeed')


    test()
