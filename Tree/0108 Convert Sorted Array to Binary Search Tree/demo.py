from typing import List, Optional


class TreeNode(object):
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root
