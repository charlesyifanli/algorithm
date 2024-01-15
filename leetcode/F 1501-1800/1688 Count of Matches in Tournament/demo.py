class Solution(object):
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2
            n = n // 2 if n % 2 == 0 else n // 2 + 1
        return res


'''
    def numberOfMatches(self, n: int) -> int:
        return n - 1
'''

if __name__ == '__main__':
    print(Solution().numberOfMatches(7))  # 6
    print(Solution().numberOfMatches(14))  # 13
