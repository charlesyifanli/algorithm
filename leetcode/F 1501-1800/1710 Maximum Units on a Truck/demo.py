from typing import List


class Solution(object):
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for type, cnt in sorted(boxTypes, key=lambda x: -x[1]):
            res += cnt * min(truckSize, type)
            truckSize -= type
            if truckSize <= 0: break
        return res


if __name__ == '__main__':
    def test():
        # case
        box_types = [[5, 10], [2, 5], [4, 7], [3, 9]]
        truck_size = 10
        assert Solution().maximumUnits(box_types, truck_size) == 91

        print('Succeed')


    test()
