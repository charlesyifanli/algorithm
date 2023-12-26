from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            max_profit = prices[right] - prices[left] if max_profit < prices[right] - prices[left] else max_profit
            left = right if prices[right] < prices[left] else left
        return max_profit


if __name__ == '__main__':
    case = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(case))

    case = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(case))

    case = [1]
    print(Solution().maxProfit(case))
