class Solution(object):
    def minimumSum(self, num: int) -> int:
        sorted_list = sorted(x for x in str(num))
        return int(sorted_list[0] + sorted_list[3]) + int(sorted_list[1] + sorted_list[2])


if __name__ == '__main__':
    def test():
        # case
        num = 4009
        assert Solution().minimumSum(num) == 13

        # case
        num = 2932
        assert Solution().minimumSum(num) == 52

        print('Succeed')


    test()
