# t = int(input())
#
# ans = 0
#
# for i in range(t):
#
#     s = input()
#
#     a = s.split()
#
#     if a[0] == 'int':
#
#         b = a[1].split(',')  # 相似的，这个是将已经被切分（以空格为切分符）的输入字符，从数组下标为1处，取出变量名，由题目可知（去看看题目的描述）
#
#         ans += len(b) * 4  # 变量名有几个，就乘多少个 4  （这里的4，指的是4个字节）
#
#     elif a[0] == 'long':
#
#         b = a[1].split(',')  # 与上面的int类似操作
#
#         ans += len(b) * 8
#
#     elif a[0] == 'String':
#
#         b = a[1].split(',')
#
#         for x in b:
#             ans += len(x) - x.find('=') - 3
#
#         # len（x）是为获取总长度，为了放回字符串的长度，x.find('=')返回=的下标为1
#
#         # 然后名字和=的长度共占4，所以减去‘=’下标长再减去3剩下的就是字符串的长
#
#         ans -= 1  # 减去后面的分号
#
#     elif a[0] == 'long[]':
#
#         s = s.lstrip('long[]')  # 去除前面的"long[]"后为形成新的字符串
#
#         b = s.split(',')  # 将函数的类型与变量定义分离，然后形成list装住
#
#         for j in b:
#             st = j.find('[') + 1  # 例如这是分离后的-- int a[20] -->找到'['的下标 再加1就是 第一个数字的位置
#
#             end = j.find(']')  # 找到结束位置，[:] 的划分是取左不取右
#
#             x = int(j[st:end])
#
#             ans += x * 8
#
#     elif a[0] == 'int[]':
#
#         s = s.lstrip('int[]')
#
#         b = s.split(',')
#
#         for j in b:
#             st = j.find('[') + 1  # 与上面类似
#
#             end = j.find(']')
#
#             x = int(j[st:end])
#
#             ans += x * 4
#
# G = ans // (1024 ** 3)
#
# M = ans % (1024 ** 3) // (1024 ** 2)
#
# K = ans % (1024 ** 2) // 1024
#
# B = ans % 1024
#
# if G != 0:
#     print(f'{G}GB', end='')
#
# if M != 0:
#     print(f'{M}MB', end='')
#
# if K != 0:
#     print(f'{K}KB', end='')
#
# if B != 0:
#     print(f'{B}B', end='')
import re

s = 'ca012sc19mf'
x = re.findall(r'\d+', s)
print(x)
