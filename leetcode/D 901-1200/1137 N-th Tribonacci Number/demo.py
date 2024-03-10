class Solution(object):
    def tribonacci(self, n: int) -> int:
        first_3 = {0: 0, 1: 1, 2: 1}
        if n in first_3.keys():
            return first_3.get(n)
        else:
            dp = [0, 1, 1]
            for i in range(3, n + 1):
                dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
            return dp[-1]
