class Solution(object):
    def is_palindrome(self, str_: str) -> bool:
        str_ = ''.join([x for x in str_ if x.isalpha()]).lower()
        return str_ == str_[::-1]


if __name__ == '__main__':
    def test_is_palindrome():
        case = "A man, a plan, a canal: Panama"
        assert Solution().is_palindrome(case) == True

        case = "race a car"
        assert Solution().is_palindrome(case) == False

        case = "0P"
        assert Solution().is_palindrome(case) == True

        print('Succeed')


    test_is_palindrome()
