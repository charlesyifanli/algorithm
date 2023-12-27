class Solution(object):
    def isPalindrome(self, s: str):
        s = ''.join(i for i in s if i.isalnum()).upper()
        return s[:len(s) >> 1] == s[:-(len(s) >> 1) - 1:-1]


if __name__ == '__main__':
    case = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(case))

    case = "race a car"
    print(Solution().isPalindrome(case))

    case = "0P"
    print(Solution().isPalindrome(case))
