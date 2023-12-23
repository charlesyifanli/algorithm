from typing import List


class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0, 0
        new_num = []
        while p1 < m or p2 < n:
            if p1 == m:
                new_num.append(nums2[p2])
                p2 += 1
                continue
            elif p2 == n:
                new_num.append(nums1[p1])
                p1 += 1
                continue
            elif nums1[p1] < nums2[p2]:
                new_num.append(nums1[p1])
                p1 += 1
            else:
                new_num.append(nums2[p2])
                p2 += 1
        for i, num in enumerate(new_num):
            nums1[i] = num


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
