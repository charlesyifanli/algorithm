class Solution(object):
    def take_model(self) -> None:
        count = int(input())
        res = []
        for i in range(count):
            n, m = list(map(int, input().split()))
            res.append(self.helper(n, m))
        for val in res:
            print(val)

    def helper(self, n: int, m: int) -> str:
        for i in range(1, m + 1):
            if n % i != i - 1: return 'Yes'
        return 'No'


Solution().take_model()
