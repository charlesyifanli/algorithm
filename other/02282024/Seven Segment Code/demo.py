import itertools

dict_ = {'a': ['f', 'b'], 'b': ['a', 'c', 'g'], 'c': ['b', 'd', 'g'],
         'd': ['e', 'c'], 'e': ['d', 'f', 'g'], 'f': ['a', 'e', 'g'],
         'g': ['b', 'c', 'e', 'f']}
s = 'abcdefg'  # 总数
ans = []  # 给方案的次数准备一个列表
cnt = 0  # 初始化次数为0
# 先找出全排列 在去全排列里筛选、
for i in range(1, 8):  # 在0-7 即1-8的顺序筛选
    for x in itertools.combinations(s, i):
        ans.append("".join(x))

for str_ in ans:
    if len(str_) == 1:
        cnt += 1
        continue

    for situation in itertools.permutations(str_):  # itertools.permutations(a, b) 连续返回由a元素生成的长度为b的全排列组合
        for c in range(1, len(situation)):
            if situation[c - 1] not in dict_[situation[c]]:
                break
        else:
            cnt += 1  # 自增操作
            break

print(cnt)
