from typing import List


class Solution(object):
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = sum(range(1, len(nums) + 1))
        num = total - sum(set(nums))
        diff = total - sum(nums)
        return [num - diff, num]


if __name__ == '__main__':
    def test():
        # case
        nums = [1, 2, 2, 4]
        assert Solution().findErrorNums(nums) == [2, 3]

        # case
        nums = [2, 2]
        assert Solution().findErrorNums(nums) == [2, 1]

        print('Succeed')


    test()
