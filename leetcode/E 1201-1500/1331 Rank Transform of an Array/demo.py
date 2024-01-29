from typing import List


class Solution(object):
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_list = sorted(list(set(arr)))
        dict_ = {}
        for idx, val in enumerate(sorted_list):
            dict_[val] = idx + 1
        for i in range(len(arr)):
            arr[i] = dict_[arr[i]]
        return arr


if __name__ == '__main__':
    def test():
        # case
        arr = [40, 10, 20, 30]
        assert Solution().arrayRankTransform(arr) == [4, 1, 2, 3]

        print('Succeed')


    test()
