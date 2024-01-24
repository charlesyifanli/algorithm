from typing import List


class Solution(object):
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for val in words:
            ls = val.split(separator)
            while '' in ls:
                ls.remove('')
            res += ls
        return res


if __name__ == '__main__':
    def test():
        # case
        words = ["one.two.three", "four.five", "six"]
        separator = "."
        assert Solution().splitWordsBySeparator(words, separator) == ["one", "two", "three", "four", "five", "six"]

        print('Succeed')


    test()
