class Solution(object):
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        else:
            dp = [0, 1]
            for i in range(2, n + 1):
                dp.append(dp[i - 1] + dp[i - 2])
            return dp[-1]

# class Solution(object):
#     def fib(self, n: int) -> int:
#         res = 0
#         if n == 0:
#             res = 0
#         elif n == 1:
#             res = 1
#         else:
#             res = self.fib(n - 1) + self.fib(n - 2)
#         return res
