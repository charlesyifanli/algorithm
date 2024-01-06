from typing import List


class Solution(object):
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(1, rowIndex + 1):
            temp = []
            for j in range(1, i):
                temp += [prev[j - 1] + prev[j]]
            curr = [1] + temp + [1]
            prev = curr
        return prev


if __name__ == '__main__':
    print(Solution().getRow(0))

    print(Solution().getRow(1))

    print(Solution().getRow(4))
