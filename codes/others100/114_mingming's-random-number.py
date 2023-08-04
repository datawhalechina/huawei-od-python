#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 114_mingming's-random-number.py
@time: 2023-07-28 15:49:08
@project: huawei-od-python
@desc: 114 明明的随机数
"""


def solve_method(nums):
    nums = list(set(nums))
    nums.sort()
    return nums


if __name__ == '__main__':
    assert solve_method([2, 2, 1]) == [1, 2]
    assert solve_method([3, 6, 9, 8, 2, 1, 1, 9, 8]) == [1, 2, 3, 6, 8, 9]
