# n = int(input())
# ls = []
# for i in range(n):
#     s = input().split()
#     ls.append(s)
# ls.sort(key=lambda x: (int(x[1]), int(x[2]), int(x[3])))
# for item in ls:
#     print(item[0])

# n = int(input())
# students = []
# for _ in range(n):
#     name, y, m, d = input().split()
#     students.append((name, int(y), int(m), int(d)))
#
# # 按照生日从大到小排序，如果生日相同，输入靠后的同学先输出
# students.sort(key=lambda x: (x[1], x[2], x[3]))
#
# for student in students:
#     print(student[0])

n = int(input())
students = []
for i in range(n):
    name, y, m, d = input().split()
    students.append((name, int(y), int(m), int(d), -i))

# 按照生日从大到小排序，如果生日相同，输入靠后的同学先输出
students.sort(key=lambda x: (x[1], x[2], x[3], x[4]))

for student in students:
    print(student[0])
