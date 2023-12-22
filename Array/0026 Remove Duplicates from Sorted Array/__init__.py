from typing import Tuple, List, Set, Dict, Optional


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []

        if not nums:
            return 0
        else:
            for i in range(0, len(nums)):
                if not new_nums:
                    new_nums.append(nums[0])
                if new_nums[-1] != nums[i]:
                    new_nums.append(nums[i])

        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return len(new_nums)


if __name__ == '__main__':
    print(Solution.removeDuplicates(Solution(), [1, 1, 2]))
