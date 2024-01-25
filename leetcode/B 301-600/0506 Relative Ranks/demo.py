from typing import List


class Solution(object):
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [''] * len(score)
        dict_ = {key: val for key, val in enumerate(score)}
        sorted_dict = sorted(dict_.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for idx, (key, val) in enumerate(sorted_dict):
            if idx == 0:
                res[key] = 'Gold Medal'
            elif idx == 1:
                res[key] = 'Silver Medal'
            elif idx == 2:
                res[key] = 'Bronze Medal'
            else:
                res[key] = '{}'.format(idx + 1)
        return res


if __name__ == '__main__':
    def test():
        # case
        score = [5, 4, 3, 2, 1]
        assert Solution().findRelativeRanks(score) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

        # case
        score = [10, 3, 8, 9, 4]
        assert Solution().findRelativeRanks(score) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

        print('Succeed')


    test()
