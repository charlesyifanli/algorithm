from typing import List


class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(sorted_intervals[i][1], res[-1][1])
            else:
                res.append([sorted_intervals[i][0], sorted_intervals[i][1]])
        return res


if __name__ == '__main__':
    def test():
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]

        intervals = [[1, 4], [4, 5]]
        assert Solution().merge(intervals) == [[1, 5]]

        print('Succeed')


    test()
