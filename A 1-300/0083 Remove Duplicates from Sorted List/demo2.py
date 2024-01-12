from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    def test_delete_duplicates():
        obj = ListNode(1)
        obj.next = ListNode(1)
        obj.next.next = ListNode(1)
        obj.next.next.next = ListNode(2)
        obj.next.next.next.next = ListNode(3)
        Solution().deleteDuplicates(obj)
        while obj:
            print(obj.val)
            obj = obj.next


    test_delete_duplicates()
