#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 116_lowest-order.py
@time: 2023-07-28 16:14:43
@project: huawei-od-python
@desc: 116 最低位排序
"""


def solve_method(nums):
    nums.sort(key=lambda x: abs(x) % 10)
    return nums


if __name__ == '__main__':
    arr = [1, 2, 5, -21, 22, 11, 55, -101, 42, 8, 7, 32]
    assert solve_method(arr) == [1, -21, 11, -101, 2, 22, 42, 32, 5, 55, 7, 8]
