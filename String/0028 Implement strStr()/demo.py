class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    case1 = "sadbutsad"
    case2 = "sad"
    print(Solution().strStr(case1, case2))

    case1 = "leetcode"
    case2 = "leeto"
    print(Solution().strStr(case1, case2))
