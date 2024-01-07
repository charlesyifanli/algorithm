class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        dict_ = {}
        for _, val in enumerate(s):
            dict_[val] = 1 if val not in dict_ else dict_[val] + 1
        for _, val in enumerate(t):
            if val not in dict_:
                return val
            else:
                dict_[val] -= 1
                if dict_[val] < 0:
                    return val


if __name__ == '__main__':
    def test_find_the_difference():
        # case1
        s = "abcd"
        t = "abcde"
        assert Solution().findTheDifference(s, t) == 'e'

        # case2
        s = "aba"
        t = "aaba"
        assert Solution().findTheDifference(s, t) == 'a'

        print("Succeed")


    test_find_the_difference()
