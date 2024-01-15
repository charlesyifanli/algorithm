from typing import List


class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_ = {}
        for i, val in enumerate(numbers):
            if target - val in dict_:
                return [dict_[target - val] + 1, i + 1]
            dict_[val] = i
        return []
