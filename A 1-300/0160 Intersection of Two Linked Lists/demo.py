from typing import Optional


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        my_set = set()
        pa, pb = head_a, head_b
        while pa:
            my_set.add(pa)
            pa = pa.next
        while pb:
            if pb in my_set:
                return pb
            pb = pb.next
        return None
