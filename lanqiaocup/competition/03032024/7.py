from collections import Counter


def f(s: str) -> int:
    cnt = 0
    counter_dict = dict(Counter(s))
    for key, val in counter_dict.items():
        if int(key) % 2 != 0:
            cnt += val
    return cnt


if __name__ == '__main__':
    s = input()
    print(f(s))
