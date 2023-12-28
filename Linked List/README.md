## traverse linked list:

all nodes

```
        ...
        p = head
        while p:
            ...
            p = p.next
        ... 
```

not have last node

```
        ...
        p = head
        while p and p.next:
            ...
            p = p.next
        ...
```

## recursion in linked list

E.g.,

```
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None  # empty
        head.next = self.removeElements(head.next, val)  # recursive
        return head.next if head.val == val else head  # if only one node
```