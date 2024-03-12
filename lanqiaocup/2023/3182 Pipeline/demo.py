# def f(length: int, ls: list) -> int:
#     sensor = [100000] * length
#     # ls.sort(key=lambda x: x[1])
#
#     for num_, open_time_ in ls:
#         left = right = num_
#
#         while left > -1 or right < length:
#             if left > -1:
#                 sensor[left] = open_time_ + (num_ - left) if open_time_ + (num_ - left) < sensor[left] else sensor[left]
#                 left -= 1
#             if right < length:
#                 sensor[right] = open_time_ + (right - num_) if open_time_ + (right - num_) < sensor[right] else sensor[
#                     right]
#                 right += 1
#
#     return max(sensor)
#
#
# if __name__ == '__main__':
#     n, pipe_len = [int(x) for x in input().split()]
#
#     open_ls = []
#     for i in range(n):
#         num, open_time = input().split()
#         open_ls.append([int(num) - 1, int(open_time)])
#
#     time = f(pipe_len, open_ls)
#
#     print(time)

def check(mid, w, n, m):
    q = []
    cnt = 0
    for i in range(1, n + 1):
        L, S = w[i]
        if mid >= S:
            t = mid - S
            l = max(1, L - t)
            r = min(m, L + t)
            q.append((l, r))
            cnt += 1
    q.sort()

    st, ed = -1, -1
    for l, r in q:
        if l <= ed + 1:
            ed = max(ed, r)
        else:
            st, ed = l, r
    return st == 1 and ed == m


def main():
    n, m = map(int, input().split())
    w = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
    l, r = 0, int(2e9)
    while l < r:
        mid = (l + r) // 2
        if check(mid, w, n, m):
            r = mid
        else:
            l = mid + 1
    print(r)


if __name__ == "__main__":
    main()
