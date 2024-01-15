from typing import List


class Solution(object):
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for val in nums:
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        return even + odd


if __name__ == '__main__':
    def test():
        nums = [3, 1, 2, 4]
        print(Solution().sortArrayByParity(nums))


    test()
