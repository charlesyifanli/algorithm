class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        str_ = ''
        while i < len(word1) or j < len(word2):
            temp_str1 = word1[i] if i < len(word1) else ''
            temp_str2 = word2[j] if j < len(word2) else ''
            str_ += temp_str1 + temp_str2
            i += 1
            j += 1
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
