from typing import List


class Solution(object):
    def countBits(self, num: int) -> List[int]:
        ls = []
        for val in range(num + 1):
            bin_ = bin(val)[2:]
            bin_ = ''.join(x for x in bin_ if x == '1')
            print(len(bin_))
            ls.append(len(bin_))
        return ls


'''
class Solution(object):
    def countBits(self, num: int) -> List[int]:
        ls = []
        for val in range(num + 1):
            ls.append(len(''.join(x for x in bin(val)[2:] if x == '1')))
        return ls
'''

if __name__ == '__main__':
    print(Solution().countBits(5))
