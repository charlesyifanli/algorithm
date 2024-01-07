class Solution(object):
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2: return False
        for i in range(1, len(s)):
            if len(s) % i == 0:
                if s[:i] * (len(s) // i) == s: return True
        return False


if __name__ == '__main__':
    def test_repeated_substring_pattern():
        # case
        s = 'abcabc'
        assert Solution().repeatedSubstringPattern(s) == True

        # case
        s = 'abcabcs'
        assert Solution().repeatedSubstringPattern(s) == False

        print('Succeed')


    test_repeated_substring_pattern()
