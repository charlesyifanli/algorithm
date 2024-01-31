from typing import List


class Solution(object):
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        set_ = set()
        for i in range(len(nums) // 2):
            set_.add((nums.pop(0) + nums.pop()) / 2)
        return len(set_)


if __name__ == '__main__':
    def test():
        # case
        nums = [4, 1, 4, 0, 3, 5]
        assert Solution().distinctAverages(nums) == 2

        print('Succeed')


    test()
