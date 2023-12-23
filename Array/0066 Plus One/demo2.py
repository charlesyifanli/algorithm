from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


if __name__ == '__main__':
    case = [0]
    print(Solution().plusOne(case))

    case = [8,9]
    print(Solution().plusOne(case))

    case = [9, 9, 9]
    print(Solution().plusOne(case))
