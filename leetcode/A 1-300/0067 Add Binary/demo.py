class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))

    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))
