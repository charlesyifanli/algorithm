from typing import List


class Solution(object):
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_ = float('inf')
        res = []
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_:
                min_ = diff
                res = [[arr[i], arr[i + 1]]]
            elif diff > min_:
                continue
            else:
                res += [[arr[i], arr[i + 1]]]
        return res


if __name__ == '__main__':
    def test():
        # case
        arr = [4, 2, 1, 3]
        assert Solution().minimumAbsDifference(arr) == [[1, 2], [2, 3], [3, 4]]

        print("Succeed")


    test()
