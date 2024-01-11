from typing import List


class Solution(object):
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
    #  return max(map(lambda x: sum(x), accounts))


'''
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for obj in accounts:
            temp = 0
            for val in obj: temp += val
            max_wealth = max(max_wealth, temp)
        return max_wealth
'''
