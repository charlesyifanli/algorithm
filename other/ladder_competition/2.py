# Partially Accepted
#
# Format error
def f(n: int) -> tuple:
    max_length = 1
    n -= 1
    while n >= 0:
        max_length += 2
        n -= 2 * max_length
    return n + 2 * max_length, max_length - 2


if __name__ == '__main__':
    ls = input().split()
    n = int(ls[0])
    char = ls[1]
    remain, max_length = f(int(n))
    for i in range(max_length, 1, -2):
        print('{0:^{1:}}'.format(char * i, max_length))
    for i in range(1, max_length + 1, 2):
        print('{0:^{1:}}'.format(char * i, max_length))
    print(remain)
