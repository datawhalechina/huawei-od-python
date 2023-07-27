#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 045_sum-number.py
@time: 2023/7/27 14:39
@project: huawei-od-python
@desc: 045 去重求和
"""


def solve_method(nums, n):
    nums = sorted(set(nums))
    result = -1
    if len(nums) >= 2 * n:
        result = sum(nums[:n]) + sum(nums[-n:])

    return result


if __name__ == '__main__':
    assert solve_method([95, 88, 83, 64, 100], 2) == 342
    assert solve_method([3, 2, 3, 4, 2], 2) == -1
