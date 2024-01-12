from typing import Optional


class ListNode(object):
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


class Solution(object):
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


if __name__ == '__main__':
    def test_add_two_numbers():
        # case
        list_1 = [2, 4, 3]
        list_2 = [5, 6, 4]
        assert Solution().addTwoNumbers(list_1, list_2) == [7, 0, 8]

        # case
        list_1 = [9, 9, 9]
        list_2 = [1]
        assert Solution().addTwoNumbers(list_1, list_2) == [0, 0, 0, 1]

        print('Succeed')


    test_add_two_numbers()
