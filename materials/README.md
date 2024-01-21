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

```
907
```

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

```
0931
```

[references](https://www.geeksforgeeks.org/dynamic-programming/?ref=gcse)
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
