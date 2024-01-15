from typing import List


class Solution(object):
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for i in arr1:
            res += 1
            for j in arr2:
                if abs(i - j) <= d:
                    res -= 1
                    break
        return res


if __name__ == '__main__':
    def test():
        arr1 = [4, 5, 8]
        arr2 = [10, 9, 1, 8]
        d = 2
        assert Solution().findTheDistanceValue(arr1, arr2, d) == 2

        print('Succeed')


    test()
