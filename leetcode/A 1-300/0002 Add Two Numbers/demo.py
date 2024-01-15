from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = sentinel = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            curr_node.next = ListNode(carry % 10)
            carry //= 10
            curr_node = curr_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sentinel.next

    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        p = head
        while l1 or l2 or carry != 0:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            curr = (val_1 + val_2 + carry) % 10
            carry = (val_1 + val_2 + carry) // 10
            p.next = ListNode(curr)
        return head.next
    # time limited exceed
    '''
