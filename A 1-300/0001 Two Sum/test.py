from demo import Solution


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


if __name__ == "__main__":
    test_twoSum()
