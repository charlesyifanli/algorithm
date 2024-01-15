from itertools import combinations
from typing import List


class Solution(object):
    def tictactoe(self, moves: List[List[int]]) -> str:
        win = {7, 56, 448, 73, 146, 292, 273, 84}
        int_a, int_b = 0, 0
        for val in moves[::2]: int_a ^= (1 << val[0] * 3 + val[1])
        for val in moves[1::2]: int_b ^= (1 << val[0] * 3 + val[1])
        for val in win:
            if int_a & val == val:
                return 'A'
            elif int_b & val == val:
                return 'B'
        return 'Pending' if len(moves) < 9 else 'Draw'


'''
    def tictactoe(self, moves: List[List[int]]) -> str:
        list_0 = []
        list_1 = []
        for i in range(0, (len(moves)), 2):
            list_0.append(moves[i])
        for i in range(1, (len(moves)), 2):
            list_1.append(moves[i])
        for num, elem in enumerate(list_0):
            target = list_0[num]
            for val in list_0:
                if val != target:
                    x = (val[0] + target[0]) / 2
                    y = (val[1] + target[1]) / 2
                    if [x, y] in list_0:
                        return "A"
        for num, elem in enumerate(list_1):
            target = list_1[num]
            for val in list_1:
                if val != target:
                    x = (val[0] + target[0]) / 2
                    y = (val[1] + target[1]) / 2
                    if [x, y] in list_1:
                        return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

'''

'''
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
        if 15 in [sum(k) for k in combinations([matrix[i][j] for i, j in moves[::2]], 3)]: return "A"
        if 15 in [sum(k) for k in combinations([matrix[i][j] for i, j in moves[1::2]], 3)]: return "B"
        return "Draw" if len(moves) == 9 else "Pending"
'''
if __name__ == '__main__':
    def test_tictactoe():
        # case
        moves = [[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]
        assert Solution().tictactoe(moves) == 'A'

        # case
        moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
        assert Solution().tictactoe(moves) == 'B'

        # case
        moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
        assert Solution().tictactoe(moves) == 'Draw'

        print('Succeed')
