from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums: list[int]) -> int:
        count = sorted(Counter(nums).items(), key=lambda x: x[0])
        if len(count) == 1: return count[0][0] * count[0][1]

        dp = [0 for _ in range(len(count))]
        dp[0] = count[0][0] * count[0][1]
        if count[1][0] - 1 != count[0][0]:
            dp[1] = dp[0] + count[1][0] * count[1][1]
        else:
            dp[1] = max(dp[0], count[1][0] * count[1][1])

        for i in range(2, len(count)):
            if count[i][0] - 1 != count[i - 1][0]:
                dp[i] = dp[i - 1] + count[i][0] * count[i][1]
            else:
                dp[i] = max(dp[i - 2] + count[i][0] * count[i][1], dp[i - 1])

        return dp[-1]


# from collections import Counter


# class Solution:
#     def deleteAndEarn(self, nums: list[int]) -> int:
#         count = sorted(Counter(nums).items(), key=lambda x: x[0])
#         prev = 0
#         curr = 0
#
#         for i in range(len(count)):
#             if i == 0 or count[i][0] - 1 != count[i - 1][0]:
#                 prev, curr = curr, curr + count[i][0] * count[i][1]
#             else:
#                 prev, curr = curr, max(prev + count[i][0] * count[i][1], curr)
#
#         return curr


if __name__ == '__main__':
    assert Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
    assert Solution().deleteAndEarn([3, 4, 2]) == 6
