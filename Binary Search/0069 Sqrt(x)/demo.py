class Solution(object):

    def mySqrt(self, x: int) -> int:
        left, right, res = 0, x, 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res


if __name__ == '__main__':
    print(Solution().mySqrt(8))
