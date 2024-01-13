from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # important code
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    def test_three_sum():
        nums = [-1, 0, 1, 2, -1, -4]
        print(Solution().threeSum(nums))

        nums = [0, 0, 0]
        print(Solution().threeSum(nums))


    test_three_sum()
