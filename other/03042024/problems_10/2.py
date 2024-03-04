cnt = 0
for i in range(101):
    for j in range(101):
        if j - i >= 10:
            cnt += 1
print(cnt)
