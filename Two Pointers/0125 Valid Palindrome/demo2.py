class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        s = s.upper()
        r = len(s) // 2
        l = r - 1 if len(s) % 2 == 0 else r
        while l > -1:
            if s[l] == s[r]:
                l -= 1
                r += 1
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
