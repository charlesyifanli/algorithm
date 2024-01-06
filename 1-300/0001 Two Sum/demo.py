class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], index]
            num_dict[num] = index
        return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result[0]} and {result[1]}")
else:
    print("No such pair found.")
