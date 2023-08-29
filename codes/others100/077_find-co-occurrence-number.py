#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 077_find-co-occurrence-number
@time:  2023/8/23 20:25
@project:  huawei-od-python
@desc: 077 找出两个整数数组中同时出现的整数
"""
from collections import Counter, defaultdict


def solve_method(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    c = c1 & c2
    if not c:
        return "NULL"
    else:
        freq_num = defaultdict(list)
        # 得到每个次数下对应的整数
        for k, v in c.items():
            freq_num[v].append(k)

        # 对次数按从小到大排序
        freq_num = dict(sorted(freq_num.items(), key=lambda x: x[0]))
        # 将每个次数下的整数从小到大排序
        freq_num = {k: sorted(v) for k, v in freq_num.items()}

        result = [f"{k}:" + ",".join(map(str, v)) for k, v in freq_num.items()]
        return result


if __name__ == '__main__':
    nums1 = [5, 3, 6, -8, 0, 11]
    nums2 = [2, 8, 8, 8, -1, 15]
    assert solve_method(nums1, nums2) == "NULL"

    nums1 = [5, 8, 11, 3, 6, 8, 8, -1, 11, 2, 11, 11]
    nums2 = [11, 2, 11, 8, 6, 8, 8, -1, 8, 15, 3, -9, 11]
    assert solve_method(nums1, nums2) == ["1:-1,2,3,6", "3:8,11"]
