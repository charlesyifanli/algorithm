def f(n, a, b, c):
    # Base cases
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        # Recursive case
        return f(n - a, a, b, c) + f(n - b, a, b, c) + f(n - c, a, b, c)


if __name__ == '__main__':
    n = int(input())
    a, b, c = list(map(int, input().split()))
    print(f(n, a, b, c))
