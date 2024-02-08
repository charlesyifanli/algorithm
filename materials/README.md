### Program = Data Structure  + Algorithm✨✨

```
Data structure is like a container while algorithm is around CRUD.  
```

```
Data structure describes the logical relationship between elements, 
and decides how to use the phisical address.

Logical structure: 
Set structure, linear structure, tree structure, graph structure

Phisical structure:
Sequential storage structure, linked storage structure, index access structure, hash access structure 
```

```
Algorithm focuses on efficiently performing CRUD operations,
balancing both time and space resources effectively.
```

### References✨✨

<details>
   <summary>Heap</summary>

```

```

[references](https://www.geeksforgeeks.org/heap-data-structure/?ref=gcse)
</details>

<br>

<details>
   <summary>Stack</summary>

[stack](https://www.geeksforgeeks.org/stack-in-python/)

[monotonic stack](https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/?ref=gcse)

#### template

```
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    for i, val in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < val:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return res
```

```
leetcode: 84, 42, 739
```

</details>

<br>

<details>
   <summary>Queue</summary>

```

```

[Queue](https://www.geeksforgeeks.org/queue-data-structure/?ref=gcse)
</details>

<br>

<details>
   <summary>Dynamic Programming</summary>

[dp](https://www.geeksforgeeks.org/dynamic-programming/?ref=gcse)

#### template

```
leetcode: 931
```

</details>

<br>

<details>
   <summary>DFS</summary>

```

```

[references](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=gcse)
</details>

<br>


<details>
   <summary>BFS</summary>

```

```

[references](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=gcse)
</details>

<br>

<details>
   <summary>Hash</summary>

```

```

[references](https://www.geeksforgeeks.org/hashing-data-structure/?ref=gcse)
</details>

<br>

<details>
   <summary>Recursion</summary>

```

```

[references](https://www.geeksforgeeks.org/recursion-in-python/?ref=gcse)
</details>

<br>
<details>
   <summary>Linked List</summary>

```

```

[references](https://www.geeksforgeeks.org/linked-list-set-1-introduction/?ref=gcse)
</details>

<br>

<details>
   <summary>BST</summary>

```

```

[references](https://www.geeksforgeeks.org/introduction-to-binary-search-tree-data-structure-and-algorithm-tutorials/?ref=gcse)
</details>

<br>

<details>
   <summary>Bitwise Algorithms</summary>

```

```

[references](https://www.geeksforgeeks.org/bitwise-algorithms/?ref=gcse)
</details>

<br>
