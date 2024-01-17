from typing import List
from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = Counter(arr)
        keys = dict_.keys()
        set_ = set()
        for key in keys:
            if dict_[key] in set_: return False
            set_.add(dict_[key])
        return True


if __name__ == '__main__':
    def test():
        # case
        arr = [1, 2, 2, 1, 1, 3]
        assert Solution().uniqueOccurrences(arr) == True

        arr = [1, 2]
        assert Solution().uniqueOccurrences(arr) == False

        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        assert Solution().uniqueOccurrences(arr) == True

        print('Succeed')


    test()
