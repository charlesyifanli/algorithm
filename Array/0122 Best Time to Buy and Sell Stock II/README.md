## description:

![q.png](assets/q.png)
![a.png](assets/a.png)

## understanding

Input:一个正整数数组<br>
Operation:找差值的和<br>
Output:四个元素两两差值的和最大，并且区间不能重合

## demo(not passed)

借鉴0121， 一个指针将数组分成两部分，
两部分分别丢给函数，然后和相加，取最大值

错误更正：不一定是两个部分，可能是多个部分

```
tc:O(n²)
sc:O(1)
```
