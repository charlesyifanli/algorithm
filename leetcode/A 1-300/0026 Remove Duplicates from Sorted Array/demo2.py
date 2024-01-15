from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


if __name__ == '__main__':
    case = [1, 1, 2]
    print(Solution().removeDuplicates(case), end="--")
    print(case)

    case2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(case2), end="--")
    print(case2)
