from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        return curr


if __name__ == '__main__':
    case, val = [3, 2, 2, 3], 3
    print(Solution().removeElement(case, val), end='--')
    print(case)

    case, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    print(Solution().removeElement(case, val), end='--')
    print(case)
