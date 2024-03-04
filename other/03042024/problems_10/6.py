def f(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        return min(f(n - 1), f(n - 2), f(n - 3)) + 1


if __name__ == '__main__':
    n = int(input())
    print(f(n))
