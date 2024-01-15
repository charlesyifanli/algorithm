from typing import List


class Solution(object):
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for val in nums:
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        for i in range(len(nums)):
            nums[i] = even.pop() if i % 2 == 0 else odd.pop()
        return nums


if __name__ == '__main__':
    def test():
        nums = [4, 2, 5, 7]
        print(Solution().sortArrayByParityII(nums))


    test()
