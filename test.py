class Solution(object):
    @staticmethod
    def f(s: str) -> str:
        return ''.join(x for x in s if x.isnumeric())


if __name__ == '__main__':
    print(Solution.f('a1b2c3d4e5f6g7h8i9j0'))
