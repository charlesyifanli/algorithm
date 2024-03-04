import math

n, Q = map(int, input().split())
fractions = [list(map(int, input().split())) for _ in range(n)]

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    num1, den1 = fractions[a]
    num2, den2 = fractions[b]
    # 计算分子和分母的和
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    # 计算最大公约数并简化分数
    gcd = math.gcd(num, den)
    num //= gcd
    den //= gcd
    print(f"{num}/{den}")
