#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 226_elegant-array.py
@time: 2023/7/27
@project: huawei-od-python
@desc: 226 优雅数组
"""
from collections import defaultdict


def solve_method(arr, k):
    res = 0
    n = len(arr)
    # i是子数组起点
    for i in range(n):
        # 统计arr元素出现次数字典，key为元素值，value为出现次数
        count = defaultdict(int)

        # j是子数组终点
        for j in range(i, n):
            key = arr[j]
            # 增加元素值的出现次数
            count[key] += 1
            # 出现了k次，即记录满足要求的子数组个数
            if count[key] >= k:
                # 自坐标j后的子数组均满足要求
                res += n - j
                break

    return res


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 1, 2, 3, 1], 3) == 1
    assert solve_method([1, 2, 3, 1, 2, 3, 1], 2) == 10
