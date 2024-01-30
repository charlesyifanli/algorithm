from typing import List


class Solution(object):
    def checkIfExist(self, arr: List[int]) -> bool:
        set_ = set()
        for i in range(len(arr)):
            if 2 * arr[i] in set_ or arr[i] / 2 in set_:
                return True
            else:
                set_.add(arr[i])
        return False


if __name__ == '__main__':
    def test():
        # case
        arr = [7, 1, 14, 11]
        assert Solution().checkIfExist(arr) == True

        arr = [-10, 12, -20]
        assert Solution().checkIfExist(arr) == True

        arr = [0, 0]
        assert Solution().checkIfExist(arr) == True

        print('Succeed')


    test()
