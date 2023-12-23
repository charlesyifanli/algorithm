## understanding

Input:两个非严格递增的整数数组，两个数组的需要合并的元素个数<br>
Operation:将一个数组按照非严格递增合并到另一个，目标数组长度足够<br>
Output:无

## demo

被合并的数组需要一个判断指针。<br>
目标数组的指针除了赋值还要比较

```
time: O(m+n)
space: O(m+n)
```

## demo2(least codes)

暴力将两个数组融合在一起，然后使用排序函数。

```
time: O((m+n)log(m+n))
space: O(1)
```

## demo3(recommended)

the same as demo, but no more space

```
time: O(m+n)
space: O(1)
```

