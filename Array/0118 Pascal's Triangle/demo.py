from typing import List


class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        temp = []
        for i in range(numRows):
            if i == 0:
                temp = [1]
                res += [temp]
                continue
            new_temp = []
            for j in range(1, i):
                new_temp += [temp[j - 1] + temp[j]]
            temp = [1] + new_temp + [1]
            res += [temp]
        return res


if __name__ == '__main__':
    numRows = 1
    print(Solution().generate(numRows))

    numRows = 4
    print(Solution().generate(numRows))

    numRows = 5
    print(Solution().generate(numRows))
