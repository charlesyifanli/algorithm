from datetime import *

n = datetime(2022, 1, 1)
sum_ = 0
for i in range(0, 366):
    s = "2022%02d%02d" % (n.month, n.day)
    n += timedelta(days=1)
    if '012' in s or '123' in s or '234' in s or '345' in s:
        sum_ += 1
print(sum_)
