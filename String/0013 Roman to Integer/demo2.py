class Solution(object):
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300,
               'D': 500, 'CM': 800, 'M': 1000}
        return sum(dic.get(s[max(i - 1, 0):i + 1], dic[n]) for i, n in enumerate(s))


if __name__ == '__main__':
    case = 'III'
    print(Solution().romanToInt(case))

    case = 'LVIII'
    print(Solution().romanToInt(case))

    case = 'MCMXCIV'
    print(Solution().romanToInt(case))
