class Solution(object):
    def only_letter_num(self, s: str) -> str:
        return ''.join(x for x in s if x.isnumeric())


if __name__ == '__main__':
    print(Solution().only_letter_num("hello! 3 wo2rld!"))
