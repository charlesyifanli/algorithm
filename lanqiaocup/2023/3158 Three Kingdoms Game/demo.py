class Solution(object):
    def f(self) -> None:
        n = int(input())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        lst3 = list(map(int, input().split()))
        max_a = 0
        max_b = 0
        max_c = 0
        lst_a = []
        for i in range(n):
            a, b, c = lst1[i], lst2[i], lst3[i]
            lst_a.append(a - b - c)
        lst_a.sort(reverse=True)
        # 前缀和优化(将时间复杂度降至O(n))
        for i in range(1, n):
            lst_a[i] += lst_a[i - 1]
        for i in range(n):
            if lst_a[i] <= 0:
                break
        max_a = i
        lst_b = []
        for i in range(n):
            a, b, c = lst1[i], lst2[i], lst3[i]
            lst_b.append(b - a - c)
        lst_b.sort(reverse=True)
        for i in range(1, n):
            lst_b[i] += lst_b[i - 1]
        for i in range(n):
            if lst_b[i] <= 0:
                break
        max_b = i
        lst_c = []
        for i in range(n):
            a, b, c = lst1[i], lst2[i], lst3[i]
            lst_c.append(c - a - b)
        lst_c.sort(reverse=True)
        for i in range(1, n):
            lst_c[i] += lst_c[i - 1]
        for i in range(n):
            if lst_c[i] <= 0:
                break
        max_c = i
        result = max(max_a, max_b, max_c)
        if result == 0:
            print(-1)
        else:
            print(result)


Solution().f()
