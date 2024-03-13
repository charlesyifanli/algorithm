n = int(input())

min_ = float('inf')
for i in range(n):
    ls = input().split()
    curr = max(int(ls[0]), int(ls[1])) - min(int(ls[0]), int(ls[1]))
    min_ = curr if curr < min_ else min_

print(min_)
