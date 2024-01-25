from typing import List


class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        l1, l2 = len(nums1), len(nums2)
        i1 = i2 = 0
        while i1 < l1 and i2 < l2:
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res


'''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list(set(nums1) & set(nums2))
        for i in range(len(res)):
            count = min(nums1.count(res[i]), nums2.count(res[i]))
            while count > 1:
                res.append(res[i])
                count -= 1
        return res
        # slowly
'''

if __name__ == '__main__':
    def test():
        # case  [4, 9]
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        print(Solution().intersect(nums1, nums2))

        # case  [2, 2]
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        print(Solution().intersect(nums1, nums2))

        print('Succeed')


    test()
