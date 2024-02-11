from typing import List


class Solution(object):
    def function(self) -> None:
        n = int(input())
        ls, dp = [], [[0 for j in range(i + 1)] for i in range(n)]
        for i in range(n):
            curr = [int(x) for x in input().split()]
            ls.append(curr)


Solution().function()
