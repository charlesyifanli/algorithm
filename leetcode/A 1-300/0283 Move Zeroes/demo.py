from typing import List


class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for val in nums:
            if val != 0:
                nums[i] = val
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0

    '''
        def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        while i > 0:
            nums.append(0)
            i -= 1
    '''


if __name__ == '__main__':
    def test_move_zeroes():
        # case
        nums = [1, 0, 3]
        Solution().moveZeroes(nums)
        assert nums == [1, 3, 0]

        # case
        nums = [1, 0, 0, 3]
        Solution().moveZeroes(nums)
        assert nums == [1, 3, 0, 0]

        print('Succeed')


    test_move_zeroes()
