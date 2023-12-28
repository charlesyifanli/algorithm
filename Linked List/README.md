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
(0203)(0206)
recursion is based on loop<br>
E.g.,

```
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None  # empty
        head.next = self.removeElements(head.next, val)  # recursive
        return head.next if head.val == val else head  # if only one node
```

## fast and slow pointers
(0876)
