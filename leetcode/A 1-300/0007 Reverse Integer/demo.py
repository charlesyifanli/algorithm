class Solution(object):
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        if not (-2 ** 31 <= temp <= 2 ** 31 - 1):
            return 0
        else:
            if x < 0:
                temp = -temp
            return temp


'''
class Solution(object):
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        return temp if x > 0 and (-2 ** 31 <= temp <= 2 ** 31 - 1) else -temp if (
                    -2 ** 31 <= temp <= 2 ** 31 - 1) else 0
'''

if __name__ == '__main__':
    a = -2 ** 31
    b = 2 ** 31 - 1
    print(a)
    print(b)
    print(-2 ** 31 <= 1534236469 <= 2 ** 31 - 1)
