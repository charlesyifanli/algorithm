from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        ls.reverse()
        i = 0
        p = head
        while p:
            p.val = ls[i]
            i += 1
            p = p.next
        return head


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
