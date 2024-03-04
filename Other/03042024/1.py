# ls = input().split(',')
# new = []
# for item in ls:
#     if len(item) < 6 or len(item) > 12: continue
#     small, big, num, special = 0, 0, 0, 0
#     for chr in item:
#         if 'a' <= chr <= 'z':
#             small = 1
#         elif 'A' <= chr <= 'Z':
#             big = 1
#         elif chr.isdigit():
#             num = 1
#         elif chr in ('!', '@', '#', '$'):
#             special = 1
#         else:
#             break
#     if special == 0: continue
#     if small + big + num >= 2: new.append(item)
# for item in new:
#     print(item)
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    count_lower, count_upper, count_digit, count_special = 0, 0, 0, 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in '!@#$':
            count_special += 1
        else:
            return False
    if count_special == 0 or len([count for count in (count_lower, count_upper, count_digit) if count > 0]) < 2:
        return False

    return True


ls = input().split(',')
for item in ls:
    if check_password(item):
        print(item)
