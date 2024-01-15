class Solution(object):
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == '__main__':
    def test_to_lower_case():
        # case
        s = 'Hello world'
        assert Solution().toLowerCase(s) == 'hello world'

        # case
        s = 'HellO'
        assert Solution().toLowerCase(s) == 'hello'

        print('Succeed')


    test_to_lower_case()
