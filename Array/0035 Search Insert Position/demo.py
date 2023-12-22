from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r, mid = 0, len(nums) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r if r > mid else l


if __name__ == '__main__':
    case, val = [1, 3, 5, 6], 5
    print(Solution().searchInsert(case, val))

    case, val = [1, 3, 5, 6], 2
    print(Solution().searchInsert(case, val))

    case, val = [1, 3, 5, 6], 7
    print(Solution().searchInsert(case, val))
