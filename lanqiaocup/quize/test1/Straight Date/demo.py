from datetime import datetime, timedelta

n = datetime(2022, 1, 1)
sum_ = 0
set_ = {'012', '123', '234', '345'}
for i in range(0, 366):
    str_ = '2022{:02d}{:02d}'.format(n.month, n.day)
    # str_ = "2022%02d%02d" % (n.month, n.day)
    n += timedelta(days=1)
    if any(x in str_ for x in set_):
        sum_ += 1
print(sum_)
