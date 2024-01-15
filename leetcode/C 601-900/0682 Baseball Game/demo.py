from typing import List


class Solution(object):
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val == 'C':
                stack.pop()
            elif val == 'D':
                stack.append(stack[-1] * 2)
            elif val == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(val))
        return sum(stack)


if __name__ == '__main__':
    def test_cal_points():
        # case
        ops = ["5", "2", "C", "D", "+"]
        assert Solution().calPoints(ops) == 30

        # case
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        assert Solution().calPoints(ops) == 27

        print('Succeed')


    test_cal_points()
