def get_pref(arr: list) -> list:
    # Add a 0 at the beginning as a placeholder,
    # because in Python, arr[0-1] represents the last element, so add a 0 at the end
    pref = [0 for _ in range(len(arr) + 1)]
    pref[0] = arr[0]
    for i in range(1, len(arr)):
        pref[i] = pref[i - 1] + arr[i]
    return pref


def get_diff(arr: list) -> list:
    diff = [0 for _ in range(len(arr))]
    diff[0] = arr[0]
    for i in range(1, len(arr)):
        diff[i] = arr[i] - arr[i - 1]
    return diff


def regional_sum(arr: list, n: int, m: int) -> int:
    pref = get_pref(arr)
    return pref[m] - pref[n - 1]


def regional_add_minus(arr: list, n: int, m: int, num: int) -> list:
    diff = get_diff(arr)
    diff[n] += num
    if m != len(arr) - 1:
        diff[m + 1] -= num
    return get_pref(diff)[:len(arr)]


arr = [1, 3, 5, 7]
print('prefix >> ', get_pref(arr))
print('diff >> ', get_diff(arr))
print(regional_sum(arr, 0, len(arr) - 1))
print(regional_add_minus(arr, 0, len(arr) - 2, 4))
