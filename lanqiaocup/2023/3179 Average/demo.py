class Solution(object):
    def function(self) -> None:
        n = int(input())
        res = 0
        dict_count, dict_cost = {}, {}

        for i in range(n):
            a, b = list(map(int, input().split()))
            if a not in dict_cost:
                dict_count[a] = 1
                dict_cost[a] = [b]
            else:
                dict_count[a] += 1
                dict_cost[a].append(b)

        target = n // 10
        for key, val in dict_count.items():
            if val > target:
                dict_cost[key].sort()
                res += sum(dict_cost[key][:val - target])

        print(res)


Solution().function()
