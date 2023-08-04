#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 106_minimum-sum-of-integers.py
@time: 2023-07-26 10:22:50
@project: huawei-od-python
@desc: 106 整数对最小和
"""


import heapq


def solve_method(arr1, arr2, k):
    # 如果含有长度为1的数组，则返回该数组元素和另一个数组前k个元素的相加
    if len(arr1) == 1:
        return arr1[0] * k + sum(arr2[:k])
    elif len(arr2) == 1:
        return arr2[0] * k + sum(arr1[:k])
    sums = []
    for x in arr1:
        for y in arr2:
            heapq.heappush(sums, x + y)

    return sum(heapq.nsmallest(k, sums))


if __name__ == "__main__":
    assert solve_method([1, 1, 2], [1, 2, 3], 2) == 4
    assert solve_method([1], [1, 2, 3], 2) == 5
    assert solve_method([1, 1, 2], [1, 2, 3], 2) == 4
    assert solve_method([1, 1, 1], [1, 2, 3], 3) == 6
    assert solve_method([1, 1], [1, 2, 3], 5) == 14
    assert solve_method([1, 1], [1, 2, 3], 6) == 18
    assert solve_method([1, 2, 3, 4], [1, 2, 3], 2) == 5
