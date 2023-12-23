from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in (str(int("".join([str(x) for x in digits])) + 1))]


if __name__ == '__main__':
    case = [0]
    print(Solution().plusOne(case))

    case = [4, 3, 2, 1, 5]
    print(Solution().plusOne(case))

    case = [9, 9, 9]
    print(Solution().plusOne(case))
