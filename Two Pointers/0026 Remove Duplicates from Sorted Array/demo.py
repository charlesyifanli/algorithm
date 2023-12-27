from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        for i in range(1, len(nums)):
            if nums[curr] != nums[i]:
                nums[curr + 1] = nums[i]
                curr += 1
        return curr + 1


if __name__ == '__main__':
    case = [1, 1, 2]
    print(Solution().removeDuplicates(case), end='--')
    print(case)

    case = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(case), end='--')
    print(case)
