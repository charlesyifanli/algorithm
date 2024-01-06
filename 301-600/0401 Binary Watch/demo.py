from typing import List


class Solution(object):
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ls = []
        for i in range(12):
            for j in range(60):
                if turnedOn == bin(i).count('1') + bin(j).count('1'):
                    ls.append('{}:{:02d}'.format(i, j))
        return ls


if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
