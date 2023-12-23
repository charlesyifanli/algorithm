from typing import List


class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = 0, len(digits) - 1
        new_digits = []
        while i > -1:
            if i == len(digits) - 1:
                temp = digits[i] + 1
            else:
                temp = digits[i] + carry
            new_digits.append(temp % 10)
            carry = temp // 10
            i -= 1
        if carry != 0:
            new_digits.append(carry)
        return new_digits[::-1]


# return [int(x) for x in (str(int("".join([str(x) for x in digits])) + 1))]

if __name__ == '__main__':
    case = [0]
    print(Solution().plusOne(case))

    case = [4, 3, 2, 1, 5]
    print(Solution().plusOne(case))

    case = [9, 9, 9]
    print(Solution().plusOne(case))
