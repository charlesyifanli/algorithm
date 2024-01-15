from typing import List


class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                closest_sum = curr_sum if abs(target - curr_sum) < abs(target - closest_sum) else closest_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum


if __name__ == '__main__':
    def test():
        # case
        assert Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2

        # case
        assert Solution().threeSumClosest(nums=[0, 0, 0], target=0) == 0

        print('Succeed')


    test()
