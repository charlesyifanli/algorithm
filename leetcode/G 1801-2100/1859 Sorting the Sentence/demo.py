class Solution(object):
    def sortSentence(self, s: str) -> str:
        list_ = s.split(' ')
        list_.sort(key=lambda x: x[-1])
        return ' '.join([word[:-1] if word[-1].isdigit() else word for word in list_])


if __name__ == '__main__':
    def test():
        s = "is2 sentence4 This1 a3"
        assert Solution().sortSentence(s) == "This is a sentence"

        s = "Myself2 Me1 I4 and3"
        assert Solution().sortSentence(s) == "Me Myself and I"

        print('Succeed')


    test()
