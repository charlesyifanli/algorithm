from typing import List


class Solution(object):
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        mod = 10 ** 9 + 7
        arr = [0] + arr + [0]
        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                res += arr[j] * (i - j) * (j - k)
            stack.append(i)
        return res % mod


if __name__ == '__main__':
    def test():
        # case
        arr = [3, 1, 2, 4]
        assert Solution().sumSubarrayMins(arr) == 17

        # case
        arr = [11, 81, 94, 43, 3]
        assert Solution().sumSubarrayMins(arr) == 444

        print('Succeed')


    test()
