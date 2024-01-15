from collections import Counter


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    '''
        def isAnagram(self, s: str, t: str) -> bool:
        dict_ = {}
        for _, val in enumerate(s):
            dict_[val] = 1 if val not in dict_ else dict_[val] + 1
        for _, val in enumerate(t):
            if val not in dict_: return False
            dict_[val] -= 1
        set_ = dict_.values()
        for val in set_:
            if val != 0: return False
        return True
    '''


if __name__ == '__main__':
    def test_is_anagram():
        # case
        s = 'abc'
        t = 'bca'
        assert Solution().isAnagram(s, t) == True

        # case
        s = 'abc'
        t = 'abca'
        assert Solution().isAnagram(s, t) == False

        print('Succeed')


    test_is_anagram()
