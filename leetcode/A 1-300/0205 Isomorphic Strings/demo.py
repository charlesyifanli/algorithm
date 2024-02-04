class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_ = {}
        for i in range(len(s)):
            if s[i] not in dict_:
                if t[i] in dict_.values(): return False
                dict_[s[i]] = t[i]
            else:
                if dict_[s[i]] != t[i]:
                    return False
                else:
                    continue
        return True


if __name__ == '__main__':
    def test():
        # case
        s = "egg"
        t = "add"
        assert Solution().isIsomorphic(s, t) == True

        # case
        s = "aaabbbba"
        t = "bbbaaaba"
        assert Solution().isIsomorphic(s, t) == False

        # case
        s = "badc"
        t = "baba"
        assert Solution().isIsomorphic(s, t) == False

        print('Succeed')


    test()
