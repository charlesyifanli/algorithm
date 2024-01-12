class Solution(object):

    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = q = 0
        str_ = ''
        while p < len(word1) or q < len(word2):
            if p == len(word1):
                str_ += word2[q:]
                continue
            if q == len(word2):
                str_ += word1[p:]
                continue
            str_ += word1[p] + word2[q]
            p += 1
            q += 1
        return str_


if __name__ == '__main__':
    def test_merge_alternately():
        solution = Solution()

        # Test case 1
        str_0 = "abc"
        str_1 = "pqr"
        assert solution.mergeAlternately(str_0, str_1) == "apbqcr"

        print("All test cases pass")


    test_merge_alternately()
