import re


class Solution:
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


if __name__ == '__main__':
    case = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(case))

    case = "race a car"
    print(Solution().isPalindrome(case))

    case = "0P"
    print(Solution().isPalindrome(case))
