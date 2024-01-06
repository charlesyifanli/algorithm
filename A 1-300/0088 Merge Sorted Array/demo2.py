from typing import List


class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
