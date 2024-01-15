from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, pre = head, None
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    p = head
    while p:
        print(p.val, end='')
        p = p.next
    print()
    p = Solution().reverseList(head)
    while p:
        print(p.val, end='')
        p = p.next
