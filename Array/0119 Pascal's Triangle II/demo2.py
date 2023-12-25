from typing import List


class Solution(object):
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == '__main__':
    print(Solution().getRow(0))

    print(Solution().getRow(1))

    print(Solution().getRow(4))
