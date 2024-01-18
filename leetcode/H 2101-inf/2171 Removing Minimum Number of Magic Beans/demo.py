from typing import List


class Solution(object):
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        sum_, len_ = sum(beans), len(beans)
        return min(sum_ - val * (len_ - i) for i, val in enumerate(beans))


'''
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        return min(sum(beans) - val * (len(beans) - i) for i, val in enumerate(beans))
    # Time Limit Exceeded!
'''

if __name__ == '__main__':
    def test():
        # case
        beans = [4, 1, 6, 5]
        assert Solution().minimumRemoval(beans) == 4

        # case
        beans = [2, 10, 3, 2]
        assert Solution().minimumRemoval(beans) == 7

        print('Succeed')


    test()
