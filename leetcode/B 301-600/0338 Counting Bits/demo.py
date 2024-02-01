from typing import List


class Solution(object):
    def countBits(self, num: int) -> List[int]:
        res = []
        for val in range(num + 1):
            res.append(len(''.join([x for x in bin(val)[2:] if x == '1'])))
        return res


if __name__ == '__main__':
    def test():
        assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]

        print('Succeed')


    test()
