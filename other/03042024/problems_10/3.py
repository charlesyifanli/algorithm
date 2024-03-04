# def count_primes(n):
#     if n <= 1:
#         return 0
#
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#
#     # 标记非质数
#     for i in range(2, int(n ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False
#
#     # 统计质数数量
#     count = sum(is_prime)
#     return count
#
#
# if __name__ == '__main__':
#     cnt = count_primes(1000000)
#     print(cnt)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


def count_primes_with_digit_sum(range_start, range_end, target_sum):
    count = 0
    for number in range(range_start, range_end + 1):
        if is_prime(number) and digit_sum(number) == target_sum:
            count += 1
    return count


if __name__ == "__main__":
    range_start = 1
    range_end = 1000000
    target_sum = 23

    result = count_primes_with_digit_sum(range_start, range_end, target_sum)
    print(result)
