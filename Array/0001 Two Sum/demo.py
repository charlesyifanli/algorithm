class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []  # Return an empty list if no matching indices are found


# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result[0]} and {result[1]}")
else:
    print("No such pair found.")
