## understanding

Input: 不以0开头的整数数组或者数组只包含0元素<br>
Operation:从左到右表示一个整数，提取出来加一。<br>
Output: 返回新数组

## demo
1. 0元素特殊对待 
2. 数组从右到左遍历(条件：右指针不越界，carry要为零)
3. 逆序遍历，顺序存储，逆序数组，注意加一和carry
```
time complexity：O(n)
space complexity: O(1)
```