class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        for _, val in enumerate(s):
            if val in t:
                t = t[t.index(val) + 1:]
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isSubsequence("axc", "ahbgdc"))
