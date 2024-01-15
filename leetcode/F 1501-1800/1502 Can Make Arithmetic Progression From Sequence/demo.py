from typing import List


class Solution(object):
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != diff: return False
        return True


if __name__ == '__main__':
    def test_can_make_arithmetic_progression():
        # case
        list_ = [3, 5, 1]
        assert Solution().canMakeArithmeticProgression(list_) == True

        # case
        list_ = [3, 5, 2]
        assert Solution().canMakeArithmeticProgression(list_) == False

        print("Succeed")


    test_can_make_arithmetic_progression()
