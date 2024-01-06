from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    case, val = [3, 2, 2, 3], 3
    print(Solution().removeElement(case, val), end='--')
    print(case)

    case, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    print(Solution().removeElement(case, val), end='--')
    print(case)
