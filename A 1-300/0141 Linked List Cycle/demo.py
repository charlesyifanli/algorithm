from typing import Optional


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        p = head
        while p and p.next:
            if p in my_set:
                return True
            my_set.add(p)
            p = p.next
        return False
