from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.helper(root.left), self.helper(root.right)) + 1
