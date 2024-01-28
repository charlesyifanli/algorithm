from typing import List


class Solution(object):
    def dominantIndex(self, nums: List[int]) -> int:
        dict_ = dict()
        for idx, val in enumerate(nums):
            dict_[idx] = val
        sorted_list = sorted(dict_.items(), key=lambda x: -x[1])
        return sorted_list[0][0] if sorted_list[0][1] >= 2 * sorted_list[1][1] else -1


if __name__ == '__main__':
    def test():
        # case
        nums = [3, 6, 1, 0]
        assert Solution().dominantIndex(nums) == 1

        # case
        nums = [1, 2, 3, 4]
        assert Solution().dominantIndex(nums) == -1

        print('Succeed')


    test()
