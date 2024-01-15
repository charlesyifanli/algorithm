class Solution(object):
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0: count += 1
        return count


'''
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for val in range(low, high + 1, 1): count += 1 if val % 2 != 0 else 0
        return count
    # Time Limit Exceeded
'''

if __name__ == '__main__':
    def test_count_odds():
        # case
        low = 3
        high = 7
        assert Solution().countOdds(low, high) == 3

        # case
        low = 8
        high = 10
        assert Solution().countOdds(low, high) == 1

        print('Succeed')


    test_count_odds()
