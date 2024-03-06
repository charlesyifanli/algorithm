# Partially Accepted
#
# Format error
def f(length: int) -> tuple:
    max_num = 1
    length -= 1
    while length >= 0:
        max_num += 2
        length -= 2 * max_num
    return length + 2 * max_num, max_num - 2


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
