#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 010_the-boundary-value-of-the-matrix-element.py
@time: 2023/9/1 16:15
@project: huawei-od-python
@desc: 049 矩阵元素的边界值
"""


def solve_method(arr):
    result_lst = arr[0]
    for lst in arr[1:]:
        result_lst = [max(x, y) for x, y in zip(result_lst, lst)]

    result_lst.sort()
    return result_lst[0]


if __name__ == '__main__':
    arr = [[1, 2], [3, 4]]
    assert solve_method(arr) == 3

    arr = [[1, 2]]
    assert solve_method(arr) == 1


