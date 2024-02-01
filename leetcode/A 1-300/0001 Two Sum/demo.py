class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], index]
            num_dict[num] = index
        return []


if __name__ == "__main__":
    def test_twoSum():
        solution = Solution()

        # Test case 1: Normal case
        nums = [2, 7, 11, 15]
        target = 9
        assert solution.twoSum(nums, target) == [0, 1]

        # Test case 2: No solution
        nums = [1, 2, 3, 4]
        target = 10
        assert solution.twoSum(nums, target) == []

        # Test case 3: Negative numbers
        nums = [-1, -2, -3, -4]
        target = -6
        assert solution.twoSum(nums, target) == [1, 3]

        # Test case 4: Single number repeated
        nums = [3, 3]
        target = 6
        assert solution.twoSum(nums, target) == [0, 1]

        print("All test cases pass")


    test_twoSum()
