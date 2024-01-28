from typing import List


class Solution(object):
    def fairCandySwap(self, alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
        sum_a = sum(alice_sizes)
        sum_b = sum(bob_sizes)
        delta = (sum_a - sum_b) // 2
        alice_sizes = set(alice_sizes)
        for val in bob_sizes:
            if val + delta in alice_sizes:
                return [val + delta, val]


if __name__ == '__main__':
    def test():
        # case
        alice_sizes = [2, 4]
        bob_sizes = [1, 2, 5]
        assert Solution().fairCandySwap(alice_sizes, bob_sizes) == [4, 5]

        print('Succeed')


    test()
