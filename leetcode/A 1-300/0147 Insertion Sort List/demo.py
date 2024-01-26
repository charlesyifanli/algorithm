from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        curr = head.next
        while curr:
            if pre.val <= curr.val:
                pre = pre.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                pre.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = pre.next
        return dummy.next


'''
# insertion_sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
'''
