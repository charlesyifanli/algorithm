from typing import List


class Solution(object):
    def isMonotonic(self, nums: List[int]) -> bool:
        ascend, descend = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]: ascend += 1
            if nums[i] > nums[i + 1]: descend += 1
        return True if (ascend == 0 or descend == 0) else False


if __name__ == '__main__':
    def test_is_monotonic():
        # case
        list_ = [1, 2, 3, 3, 4]
        assert Solution().isMonotonic(list_) == True

        # case
        list_ = [8, 6, 3]
        assert Solution().isMonotonic(list_) == True

        # case
        list_ = [8, 9, 6, 3]
        assert Solution().isMonotonic(list_) == False


    print("Succeed")

    test_is_monotonic()
