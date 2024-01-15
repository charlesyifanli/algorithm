## understanding

Input: 不以0开头的整数数组或者数组只包含0元素<br>
Operation:从左到右表示一个整数，提取出来加一。<br>
Output: 返回新数组

## demo

```
逆序遍历数组，
顺序赋值新数组，特别注意carry
新数组逆序
```

```
time complexity：O(n)
space complexity: O(n)
```

## demo2

```
遇到9赋0，遇到其他加1并且直接返回
最后高位加一
```

```
time complexity：O(n)
space complexity: O(1)
```

## demo3(recommended strongly)

将数字元素拼成字符串，转成整数，加1，分割成数字元素

```
time complexity：O(n)
space complexity: O(1)
```