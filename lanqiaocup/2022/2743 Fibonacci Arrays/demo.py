# def f(len_: int, ls: list[int]):
#     if len_ < 3:
#         if ls[0] == ls[1]:
#             return 0
#         else:
#             return 1
#     res = 0
#     res_ = 0
#
#     dp = []
#     dp_ = []
#     for i in range(2):
#         dp.append(ls[0])
#         dp_.append(ls[1])
#
#     for i in range(2, len_):
#         dp.append(dp[-1] + dp[-2])  # 使用列表最后两个元素的和
#         if ls[i] != dp[-1]:  # 检查最后一个元素是否和ls[i]相等
#             res += 1
#
#         dp_.append(dp_[-1] + dp_[-2])  # 使用列表最后两个元素的和
#         if ls[i] != dp_[-1]:  # 检查最后一个元素是否和ls[i]相等
#             res_ += 1
#
#     return max(res, res_)
#
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# print(f(n, arr))

arr = [0] * 100001
fi = [0] * 100
max_count = 0


def get_fi(first):
    global items
    items = 2
    fi[0] = fi[1] = first
    for i in range(2, 100):
        fi[i] = fi[i - 1] + fi[i - 2]
        if fi[i] > 1000000:
            break
        items += 1


def contrast():
    count = 0
    for i in range(items):
        if arr[i] == fi[i]:
            count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    max_count = 0
    for i in range(1, 1000000):
        get_fi(i)
        count = contrast()
        max_count = max(max_count, count)

    print(n - max_count)
