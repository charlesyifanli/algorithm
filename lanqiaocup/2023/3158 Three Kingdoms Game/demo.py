from typing import List


class Solution(object):
    def f(self) -> int:
        n = int(input())
        input_a = list(map(int, input().split()))
        input_b = list(map(int, input().split()))
        input_c = list(map(int, input().split()))

        diff_a, diff_b, diff_c = [], [], []
        for i in range(n):
            diff_a.append(input_a[i] - input_b[i] - input_c[i])
            diff_b.append(input_b[i] - input_a[i] - input_c[i])
            diff_c.append(input_c[i] - input_b[i] - input_a[i])

        count_a = self.helper(n, diff_a)
        count_b = self.helper(n, diff_b)
        count_c = self.helper(n, diff_c)

        res = max(count_a, count_b, count_c)
        return -1 if res == 0 else res

    def helper(self, n: int, diff_i: List[int]) -> int:
        diff_i.sort(reverse=True)
        for i in range(1, n):
            diff_i[i] += diff_i[i - 1]
        for i in range(n):
            if diff_i[i] <= 0:
                return i


print(Solution().f())
