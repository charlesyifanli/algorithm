def f(s: str) -> bool:
    if len(s) < 6 or len(s) > 12: return False
    cnt_lower, cnt_upper, cnt_digit, cnt_special = 0, 0, 0, 0
    for char in s:
        if char.islower():
            cnt_lower += 1
        elif char.isupper():
            cnt_upper += 1
        elif char.isdigit():
            cnt_digit += 1
        elif char in '!@#$':
            cnt_special += 1
        else:
            return False
    if cnt_special == 0 or len([x for x in (cnt_lower, cnt_upper, cnt_digit) if x > 0]) < 2:
        return False
    return True


if __name__ == '__main__':
    ls = input().split(',')
    for item in ls:
        if f(item):
            print(item)
