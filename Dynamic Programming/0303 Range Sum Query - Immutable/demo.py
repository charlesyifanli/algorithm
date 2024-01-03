from typing import List


# Prefix Sum
class NumArray(object):
    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]


'''
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        curr_num = self.nums[left] + self.nums[right]
        if left > right: return 0
        if left == right: return self.nums[left]
        return curr_num + self.sumRange(left + 1, right - 1)
    Worse time complexity: from O(n) to O(n log n)!!!
'''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
