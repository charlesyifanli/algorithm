from typing import List


class Solution(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = False
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] in dict_ and abs(dict_[nums[i]] - i) <= k: res = True
            dict_[nums[i]] = i
        return res


if __name__ == '__main__':
    def test():
        # case
        nums = [1, 2, 3, 1]
        k = 3
        assert Solution().containsNearbyDuplicate(nums, k) == True

        # case
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        assert Solution().containsNearbyDuplicate(nums, k) == False

        # case
        nums = [2, 2]
        k = 3
        assert Solution().containsNearbyDuplicate(nums, k) == True

        print('Succeed')


    test()
