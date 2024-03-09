from collections import Counter

lst = [1, 2, 3, 1, 2, 3, 4, 1, 2, 1]
lst_ = [2, 1, 3, 1, 2, 3, 4, 1, 2, 1]

counter = Counter(lst)
counter_ = Counter(lst_)

print('lst == lst_? >> ' + f'{lst == lst_}')
print('counter == counter_? >> ' + f'{counter == counter_}')
