class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == '__main__':
    def test_length_of_last_word():
        # case
        s = "Hello World"
        assert Solution().lengthOfLastWord(s) == 5

        # case
        s = "   fly me   to   the moon  "
        assert Solution().lengthOfLastWord(s) == 4

        print('Succeed')


    test_length_of_last_word()
