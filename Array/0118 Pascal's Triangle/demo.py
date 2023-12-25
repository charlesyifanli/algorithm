from typing import List


class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        last_row = [1]
        res = [last_row]
        for i in range(1,numRows):
            sub_row = []
            for j in range(1, i):
                sub_row += [last_row[j - 1] + last_row[j]]
            last_row = [1] + sub_row + [1]
            res += [last_row]
        return res


if __name__ == '__main__':
    numRows = 1
    print(Solution().generate(numRows))

    numRows = 4
    print(Solution().generate(numRows))

    numRows = 5
    print(Solution().generate(numRows))
