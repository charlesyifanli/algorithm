def f(n: int, arr: list[int]) -> list[int]:
    max_val, min_val = float('inf'), -float('inf')
    for i in range(1, n - 1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            max_val = arr[i] if arr[i] < max_val else max_val
        elif arr[i] < arr[i + 1] and arr[i] < arr[i - 1]:
            min_val = arr[i] if arr[i] > min_val else min_val
        else:
            continue
    return [min_val, max_val]


if __name__ == '__main__':
    len_ = int(input())
    arr = [int(x) for x in input().split()]
    print(*f(len_, arr))
