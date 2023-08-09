#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 083_find-number.py
@time: 2023/8/9 16:35
@project: huawei-od-python
@desc: 083 找数字
"""


def solve_method(arr):
    result = 0
    n = len(arr)
    for ints in arr:
        max_sum = -1
        for i in range(n):
            # 循环左移
            bin_int = ints[i:] + ints[:i]
            max_sum = max(max_sum, int(''.join(map(str, bin_int)), 2))

        result += max_sum

    return result


if __name__ == '__main__':
    arr = [[1, 0, 0, 0, 1],
           [0, 0, 0, 1, 1],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 1, 1],
           [1, 0, 1, 0, 1]]
    assert solve_method(arr) == 122
