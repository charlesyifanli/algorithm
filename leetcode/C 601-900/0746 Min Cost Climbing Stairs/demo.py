class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
        return dp[-1]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert Solution().minCostClimbingStairs(cost) == 6
