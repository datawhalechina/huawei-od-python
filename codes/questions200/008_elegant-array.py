#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 008_elegant-array.py
@time: 2023/7/27
@project: huawei-od-python
@desc: 008 优雅数组
"""
from collections import Counter


def solve_method(arr, k):
    res = 0
    n = len(arr)
    # i是子数组起点
    for i in range(n):
        # j是子数组终点
        for j in range(i, n):
            # 记录子数组的数字频数
            counter = Counter(arr[i: j + 1])
            # 统计最大的次数是否大于等于k，是否为k-优雅数组
            if counter.most_common(1)[0][1] >= k:
                res += 1
    return res


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 1, 2, 3, 1], 3) == 1
    assert solve_method([1, 2, 3, 1, 2, 3, 1], 2) == 10
