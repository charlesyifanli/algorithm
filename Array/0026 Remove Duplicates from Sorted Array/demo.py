from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = [nums[0]]
        for i in range(0, len(nums)):
            if new_nums[-1] != nums[i]:
                new_nums.append(nums[i])
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return len(new_nums)


if __name__ == '__main__':
    case = [1, 1, 2]
    print(Solution().removeDuplicates(case), end="--")
    print(case)

    case2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(case2), end="--")
    print(case2)
