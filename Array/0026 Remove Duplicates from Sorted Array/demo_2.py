from typing import Tuple, List, Set, Dict, Optional


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


if __name__ == '__main__':
    print(Solution.removeDuplicates(Solution(), [1, 1, 2]))
