from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            curr_profit = prices[right] - prices[left]
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[left] > prices[right]:
                left = right
        return max_profit
