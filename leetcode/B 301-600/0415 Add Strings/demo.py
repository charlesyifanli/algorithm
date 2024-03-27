import sys


class Solution(object):
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10 ** 5)
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    assert Solution().addStrings('11', '123') == '134'
