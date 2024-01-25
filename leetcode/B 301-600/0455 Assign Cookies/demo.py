from typing import List


class Solution(object):
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        cookie = 0
        while cookie < len(s) and count < len(g):
            if g[count] <= s[cookie]:
                count += 1
            cookie += 1
        return count


if __name__ == '__main__':
    def test():
        # case
        g = [1, 2]
        s = [1, 2, 3]
        assert Solution().findContentChildren(g, s) == 2

        # case
        g = [1, 2, 3]
        s = [1, 1]
        assert Solution().findContentChildren(g, s) == 1

        print('Succeed')


    test()
