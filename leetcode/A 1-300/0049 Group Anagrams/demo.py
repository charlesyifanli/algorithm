from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        for i, val in enumerate(strs):
            key = ''.join(sorted(val))
            if key in dict_.keys():
                dict_[key].append(val)
            else:
                dict_[key] = [val]
        return list(dict_.values())


if __name__ == '__main__':
    def test():
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(Solution().groupAnagrams(strs))


    test()
