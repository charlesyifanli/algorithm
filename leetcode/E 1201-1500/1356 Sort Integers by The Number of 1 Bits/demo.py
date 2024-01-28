from typing import List


class Solution(object):
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 使用哈希表（字典），建立 <二进制1的次数, [数字1， 数字2，...]>的映射
        d = dict()
        for x in arr:
            b = bin(x)  # 把 x 转出二进制字符串
            cnt = b.count('1')  # 统计二进制中 '1' 的个数
            # print('cnt = ', cnt)
            if cnt not in d:
                # 不存在值为 cnt 的key，建立 <cnt, []>的映射关系
                d[cnt] = list()
            d[cnt].append(x)
        # 将字典 d 按 key（1的出现次数）进行排序
        keys = sorted(d.keys())
        ans = list()
        for k in keys:
            # 对 list 进行排序
            ans += sorted(d[k])
            # print('k = ', k)
        return ans


if __name__ == '__main__':
    def test():
        # case
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        assert Solution().sortByBits(arr) == [0, 1, 2, 4, 8, 3, 5, 6, 7]

        print('Succeed')


    test()
