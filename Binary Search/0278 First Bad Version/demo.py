# The isBadVersion API is already defined for you.

def isBadVersion(version: int) -> bool:
    return False


class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        left, right, res = 1, n, 0
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
                res = right + 1
            else:
                left = mid + 1
                res = left
        return res
