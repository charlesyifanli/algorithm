def f(suppose: str, true: str) -> int:
    res = 0
    suppose, true = list(suppose), list(true)
    for i in range(1, len(true) - 1):
        if true[i] != suppose[i]:
            if true[i - 1] == true[i + 1] and true[i] != true[i - 1]:
                true[i] = true[i + 1]
                res += 1
        else:
            continue
    return res if suppose == true else -1


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s, t = input(), input()
        print(f(s, t))
