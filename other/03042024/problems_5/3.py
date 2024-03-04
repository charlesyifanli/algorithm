ls = []
for i in range(12):
    ls.append(int(input()))
remain = 0
bank = 0
for idx, budget in enumerate(ls):
    remain = 300 + remain - budget
    if 0 <= remain < 100:
        continue
    elif remain < 100:
        print(-1 * (idx + 1))
        break
    else:
        temp = remain // 100
        remain %= 100
        bank += temp * 100
    if idx == 11:
        remain += bank * (1 + 0.2)
        print(int(remain))
