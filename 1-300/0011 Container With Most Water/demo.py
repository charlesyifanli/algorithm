class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            length = r - l
            high = 0
            if height[l] < height[r]:
                high = height[l]
                l += 1
            else:
                high = height[r]
                r -= 1

            if length * high > max_area:
                max_area = length * high

        return max_area


# Test cases
test_cases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],  # expected output: 49
    [4, 3, 2, 1, 4],  # expected output: 16
    [1, 2, 1],  # expected output: 2
]

# Evaluate test cases
solution = Solution()
for i, test_case in enumerate(test_cases):
    result = solution.maxArea(test_case)
    print(f"Test case {i + 1}: Input {test_case}, Output {result}")
