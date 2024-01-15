from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, val in enumerate(nums):
            if val >= target: return i
        return len(nums)


if __name__ == '__main__':
    case, val = [1, 3, 5, 6], 5  # 2
    print(Solution().searchInsert(case, val))

    case, val = [1, 3, 5, 6], 2  # 1
    print(Solution().searchInsert(case, val))

    case, val = [1, 3, 5, 6], 7  # 4
    print(Solution().searchInsert(case, val))
