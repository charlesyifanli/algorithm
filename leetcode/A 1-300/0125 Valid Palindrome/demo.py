import re


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s if x.isalnum()).upper()
        return s == s[::-1]


'''
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(lambda x: x.isalnum(), s)).upper()
        right = len(s) // 2
        left = right - 1 if len(s) % 2 == 0 else right
        while right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return False
        return True
'''

'''
    def isPalindrome(self, s: str) -> bool:
        s = re.compile(r'[^a-zA-Z0-9]').sub('', s).upper()
        right = len(s) // 2
        left = right - 1 if len(s) % 2 == 0 else right
        while right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return False
        return True
'''

if __name__ == '__main__':
    def test_is_palindrome():
        case = "A man, a plan, a canal: Panama"
        assert Solution().isPalindrome(case) == True

        case = "race a car"
        assert Solution().isPalindrome(case) == False

        case = "0P"
        assert Solution().isPalindrome(case) == False

        print('Succeed')


    test_is_palindrome()
