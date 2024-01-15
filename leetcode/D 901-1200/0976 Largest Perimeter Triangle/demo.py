from typing import List


class Solution(object):
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            if self.is_tri(nums[-3:]):
                return sum(nums[-3:])
            else:
                nums.pop()
        return 0

    def is_tri(self, tri: List[int]) -> bool:
        tri.sort()
        return True if tri[0] + tri[1] > tri[2] else False


'''
    # Time Limit Exceeded
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    perimeter = nums[j] + nums[k] + nums[i]
                    if nums[j] + nums[k] > nums[i] and perimeter > res:
                        res = nums[j] + nums[k] + nums[i]
                        break
        return res
'''

if __name__ == '__main__':
    def test():
        nums = [2, 1, 2]
        assert Solution().largestPerimeter(nums) == 5

        print('Succeed')


    test()
