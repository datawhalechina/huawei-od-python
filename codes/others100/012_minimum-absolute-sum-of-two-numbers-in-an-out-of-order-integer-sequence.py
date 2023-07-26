#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 012_minimum-absolute-sum-of-two-numbers-in-an-out-of-order-integer-sequence.py
@time: 2023/7/26 19:25
@project: huawei-od-python
@desc: 012 乱序整数序列两数之和绝对值最小
"""
import math


def solve_method(nums):
    min_value = math.inf
    min_num = 0
    max_num = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            a, b = nums[i], nums[j]
            if a != b:
                value = abs(a + b)
                if value < min_value:
                    min_value = value
                    min_num = min(a, b)
                    max_num = max(a, b)

    return [min_num, max_num, min_value]


if __name__ == '__main__':
    assert solve_method([-1, -3, 7, 5, 11, 15]) == [-3, 5, 2]
