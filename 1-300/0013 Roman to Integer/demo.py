class Solution(object):
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res


if __name__ == '__main__':
    case = 'III'
    print(Solution().romanToInt(case))

    case = 'LVIII'
    print(Solution().romanToInt(case))

    case = 'MCMXCIV'
    print(Solution().romanToInt(case))
