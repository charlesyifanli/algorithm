# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         length = len(nums)
#         result = []
#
#         for index in range(length - 2):
#             if index > 0 and nums[index] == nums[index - 1]:
#                 continue
#
#             start, end = index + 1, length - 1
#
#             while start < end:
#                 total = nums[index] + nums[start] + nums[end]
#                 if total == 0:
#                     result.append([nums[index], nums[start], nums[end]])
#                     while start < end and nums[start] == nums[start + 1]:
#                         start += 1
#                     while start < end and nums[end] == nums[end - 1]:
#                         end -= 1
#                     start += 1
#                     end -= 1
#                 elif total < 0:
#                     start += 1
#                 else:
#                     end -= 1
#
#         return result
#
#
# # Test case
# solution = Solution()
# arr = [-1, 0, 1, 2, -1, -4]
# arr1 = solution.threeSum(arr)
#
# for triplet in arr1:
#     print(*triplet)
