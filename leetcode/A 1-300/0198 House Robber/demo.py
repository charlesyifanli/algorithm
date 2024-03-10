class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums[:2])
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    assert Solution().rob([0]) == 0
    assert Solution().rob([2, 1, 1, 2]) == 4
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
