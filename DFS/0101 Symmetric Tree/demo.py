from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.recursion(root.left, root.right)

    def recursion(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left or not right: return left == right
        return left.val == right.val and self.recursion(left.left, right.right) and self.recursion(left.right,right.left)
