from typing import List


class Solution(object):
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


if __name__ == '__main__':
    def test():
        # case
        arr = [30, 60, 90]
        assert Solution().dailyTemperatures(arr) == [1, 1, 0]

        # case
        arr = [73, 74, 75, 71, 69, 72, 76, 73]
        assert Solution().dailyTemperatures(arr) == [1, 1, 4, 2, 1, 1, 0, 0]

        print('Succeed')


    test()
