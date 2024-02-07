class Solution(object):
    a = int(input())
    def same_add(m, n):
        for i in range(1, m + 1):
            if n % i != i - 1:
                return "Yes"
        return "No"
    for i in range(a):
        n, m = list(map(int, input().split(" ")))
        print(same_add(m, n))

    # def take_model(self):
    #     res = []
    #     n = int(input())
    #     for i in range(n):
    #         list_ = list(map(int, input().split()))
    #         n, m = list_[0], list_[1]



Solution().take_model()
