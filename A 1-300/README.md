# ideas

## python

```
在 Python 3.5 引入类型提示后，typing 库提供了一组用于定义类型的工具，
包括各种类型（如List、Tuple、Dict等），以及用于泛型编程的工具（如Union、Optional等）。
这些工具有助于在代码中更清晰地表达预期的数据类型，提高代码的可读性和可维护性。
```

## 0001 two sum

ideas:<br>

```
01----O(n²)
肯定要遍历数组。
指针到达某一个数组元素（下标和值）后，与目标值做差。
从当前元素的下一个开始，直到最后一个元素，与差值比较。
```

```
02----O(n)
肯定要遍历数组。
利用键值对，key（数组的值） value（数组下表）。
指针到达某一个数组元素（下标和值）后，与目标值做差。
判断差值是否在map里面，不在就把这个键值对放入map。
```

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