from typing import Optional


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ls = []
        p = head
        while p and p.next:
            if p in ls:
                return True
            ls.append(p)
            p = p.next
        return False
