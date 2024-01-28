from typing import List


class Solution(object):
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        dict_ = {}
        for val in arr:
            count = bin(val).count('1')
            if count not in dict_:
                dict_[count] = [val]
            else:
                dict_[count].append(val)
        sorted_list = sorted(dict_.items(), key=lambda x: x[0])
        res = []
        for val in sorted_list:
            res += val[1]
        return res


if __name__ == '__main__':
    def test():
        # case
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        assert Solution().sortByBits(arr) == [0, 1, 2, 4, 8, 3, 5, 6, 7]

        print('Succeed')


    test()
