class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] in list(dic.values()):
                stack.append(s[i])
            else:
                if stack and stack[-1] == dic[s[i]]:
                    stack.pop()
                else:
                    return False
        return not stack


if __name__ == '__main__':
    case = "()"
    print(Solution().isValid(case))

    case = "(("
    print(Solution().isValid(case))

    case = "(]"
    print(Solution().isValid(case))

    case = "]"
    print(Solution().isValid(case))
