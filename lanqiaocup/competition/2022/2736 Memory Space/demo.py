import re


def f(s: str) -> int:
    res = 0
    ls = s.split()
    if ls[0] == 'int':
        res += 4 * len(ls[1].split(','))
    elif ls[0] == 'long':
        res += 8 * len(ls[1].split(','))
    elif ls[0] == 'int[]':
        sum_ = 0
        for item in ls:
            sum_ += sum(re.findall(r'\d+', item))
        res += sum_ * 4
    elif ls[0] == 'long[]':
        sum_ = 0
        for item in ls:
            print(item)
            sum(re.findall(r'\d+', item))
        res += sum_ * 8
    else:  # ls[0] == 'String'
        temp_ls = ls[1].split(',')
        for item in temp_ls:
            res += len(item) - item.find('=') - 3
    return res


def g(size: int) -> str:
    s = ''
    return s


if __name__ == '__main__':
    byte_size = 0
    n = int(input())

    for i in range(n):
        byte_size += f(input())

    print(byte_size)
    print(g(byte_size))
