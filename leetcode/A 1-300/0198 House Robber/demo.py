class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [[0, nums[0]] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])


if __name__ == '__main__':
    assert Solution().rob([2, 1, 1, 2]) == 4
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
