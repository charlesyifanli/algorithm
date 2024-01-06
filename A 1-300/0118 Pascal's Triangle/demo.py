from typing import List


class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        previous_row = [1]
        res = [previous_row]
        for i in range(1, numRows):
            current_row = [1, 1]
            for j in range(1, i):
                current_row.insert(1, previous_row[j - 1] + previous_row[j])
            res += [current_row]
            previous_row = current_row
        return res


if __name__ == '__main__':
    numRows = 1
    print(Solution().generate(numRows))

    numRows = 2
    print(Solution().generate(numRows))

    numRows = 5
    print(Solution().generate(numRows))
