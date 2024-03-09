class Solution:
    def f(self, s: str) -> int:
        cnt = 0
        i = 0
        while i < len(s) - 1:
            curr = s[i]
            late = s[i + 1]
            if '?' in [curr, late]:
                cnt += 1
                i += 2
            elif curr == late and (curr == '0' or '1'):
                cnt += 1
                i += 2
            else:
                i += 1
        return cnt


print(Solution().f(input()))
