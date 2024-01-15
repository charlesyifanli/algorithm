from typing import List


class Solution(object):
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
