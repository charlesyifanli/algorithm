from typing import List


class NumArray(object):

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        curr_num = self.nums[left] + self.nums[right]
        if left > right: return 0
        if left == right: return self.nums[left]
        return curr_num + self.sumRange(left + 1, right - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
