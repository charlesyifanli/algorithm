n = int(input())
ls = []
for i in range(n):
    name, y, m, d = input().split()
    ls.append((name, int(y), int(m), int(d), -i))
ls.sort(key=lambda x: (x[1], x[2], x[3], x[4]))

for item in ls:
    print(item[0])
