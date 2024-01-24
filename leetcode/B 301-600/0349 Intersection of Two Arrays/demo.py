from typing import List


class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    def test():
        # case
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        assert Solution().intersection(nums1, nums2) == [2]

        # case
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        assert Solution().intersection(nums1, nums2) == [4, 9] or [9, 4]

        print('Succeed')


    test()
