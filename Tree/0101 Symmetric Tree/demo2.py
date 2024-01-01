from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return None

    def recursion(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.recursion(left.left, right.right) and self.recursion(left.right, right.left)
