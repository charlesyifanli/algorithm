import re


def f(s: str) -> int:
    res = 0
    ls = s.split()

    if ls[0] == 'int':
        res += 4 * len(ls[1].split(','))

    elif ls[0] == 'long':
        res += 8 * len(ls[1].split(','))

    elif ls[0] == 'int[]':
        total = 0
        for i in range(2, len(ls)):  # 'a1=new' also has number
            num_ls = re.findall(r'\d+', ls[i])
            total += int(num_ls[0])
        res += 4 * total

    elif ls[0] == 'long[]':
        total = 0
        for i in range(2, len(ls)):  # 'a1=new' also has number
            num_ls = re.findall(r'\d+', ls[i])
            total += int(num_ls[0])
        res += 8 * total

    elif ls[0] == 'String':
        val_ls = ls[1].split(',')
        for item in val_ls:
            res += len(item) - item.find('=') - 3  # len('s12')==3
        res -= 1
    return res


def g(b: int) -> str:
    s = ''

    # GB
    g = b // (1024 ** 3)
    b %= (1024 ** 3)
    s += f'{g}GB' if g > 0 else ''

    # MB
    m = b // (1024 ** 2)
    b %= (1024 ** 2)
    s += f'{m}MB' if m > 0 else ''

    # KB
    k = b // 1024
    b %= 1024
    s += f'{k}KB' if k > 0 else ''

    # B
    s += f'{b}B' if b > 0 else ''

    return s


if __name__ == '__main__':
    byte_size = 0
    n = int(input())

    for i in range(n):
        byte_size += f(input())

    print(g(byte_size))
