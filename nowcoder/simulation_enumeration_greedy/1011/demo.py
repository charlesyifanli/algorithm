order = int(input())

mat = [[0] * order for _ in range(order)]
mat[0][order // 2] = 1

arr = [0, order // 2]

for i in range(2, order ** 2 + 1):
    if arr[0] == 0 and arr[1] != order - 1:
        arr[0] = order - 1
        arr[1] += 1
    elif arr[0] != 0 and arr[1] == order - 1:
        arr[0] = arr[0] - 1
        arr[1] = 0
    elif arr[0] == 0 and arr[1] == order - 1:
        arr[0] = 1
        arr[1] = order - 1
    elif arr[0] != 0 and arr[1] != order - 1:
        if mat[arr[0] - 1][arr[1] + 1] == 0:
            arr[0] -= 1
            arr[1] += 1
        else:
            arr[0] += 1
    mat[arr[0]][arr[1]] = i

for item in mat:
    print(*item)
