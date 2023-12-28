from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        ls = []
        while curr:
            ls.append(curr.val)
            curr = curr.next
        return ls[:len(ls) >> 1] == ls[:-(len(ls) >> 1) - 1:-1]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))
