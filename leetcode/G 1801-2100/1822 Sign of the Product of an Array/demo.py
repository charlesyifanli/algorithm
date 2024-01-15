from typing import List


def signFunc(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Solution(object):
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for val in nums:
            product *= val
        return signFunc(product)
