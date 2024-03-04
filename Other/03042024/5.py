t = int(input())
res = []
for i in range(t):
    len_ = int(input())
    s = input()
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
            continue
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    res.append(len(stack))

for i in res:
    print(i)
