from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = min(strs)
        s2 = max(strs)
        for idx, val in enumerate(s1):
            if val != s2[idx]:
                return s1[:idx]
        return s1


if __name__ == '__main__':
    def test():
        # case
        strs = ["flower", "flow", "flight"]
        assert Solution().longestCommonPrefix(strs) == 'fl'

        # case
        strs = ["dog", "racecar", "car"]
        assert Solution().longestCommonPrefix(strs) == ''

        print('Succeed')


    test()
