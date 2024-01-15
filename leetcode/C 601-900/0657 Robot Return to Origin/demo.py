class Solution(object):
    def judgeCircle(self, moves: str) -> bool:
        dict_ = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for val in moves:
            dict_[val] += 1
        return dict_['R'] == dict_['L'] and dict_['U'] == dict_['D']


if __name__ == '__main__':
    def test_judge_circle():
        # case
        moves = "UD"
        assert Solution().judgeCircle(moves) == True

        # case
        moves = "LL"
        assert Solution().judgeCircle(moves) == False

        print('Succeed')


    test_judge_circle()
