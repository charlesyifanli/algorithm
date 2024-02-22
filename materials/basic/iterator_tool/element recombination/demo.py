from itertools import combinations

ls = ['h', 'y', 'k', 'q', 's']

for i in range(2, 4):
    obj = combinations(ls, i)
    print(type(obj))
    print(list(obj))
