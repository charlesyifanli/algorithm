from typing import List


class Solution(object):
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        set_ = set()
        res = 0
        for val in words:
            if val[::-1] in set_:
                res += 1
            else:
                set_.add(val)
        return res


if __name__ == '__main__':
    def test():
        # case
        words = ["cd", "ac", "dc", "ca", "zz"]
        assert Solution().maximumNumberOfStringPairs(words) == 2

        # case
        words = ["ab", "ba", "cc"]
        assert Solution().maximumNumberOfStringPairs(words) == 1

        print('Succeed')


    test()
