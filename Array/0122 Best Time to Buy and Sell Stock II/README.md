## description:

![q.png](assets/q.png)
![a.png](assets/a.png)

## understanding

Input:一个正整数数组<br>
Operation:找差值的和<br>
Output:四个元素两两差值的和最大，并且区间不能重合

## demo

双指针，遇到小的就移动左指针，每次比较差值，
同时递归recursive

```
tc:O(n²)
sc:O(1)
```
