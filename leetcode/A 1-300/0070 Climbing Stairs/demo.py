class Solution(object):
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        a, b, temp = 1, 2, 0
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


'''
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
'''

'''
    def climbStairs(self, n: int) -> int:
     if n == 1: return 1
     if n == 2: return 2
     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
     Time Limit Exceeded!!!
     Time complexity O(2^n)
'''
