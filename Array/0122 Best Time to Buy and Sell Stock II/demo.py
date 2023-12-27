from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        for i in range(1, len(prices)):
            max_profit = max(max_profit, self.max_profit(prices[0:i + 1]) + self.max_profit(prices[i:len(prices)]))
        return max_profit

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            max_profit = prices[right] - prices[left] if prices[right] - prices[left] > max_profit else max_profit
            left = right if prices[right] < prices[left] else left
        return max_profit


if __name__ == '__main__':
    case = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(case))

    case = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(case))

    case = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(case))

    case = [3, 3, 5, 0, 0, 3, 1, 4]  # 8
    print(Solution().maxProfit(case))
