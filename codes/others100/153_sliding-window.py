#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 153_sliding-window.py
@time: 2023/8/29 0:18
@project: huawei-od-python
@desc: 153 滑动窗口
"""
import math


def solve_method(nums, window_size):
    if window_size > len(nums):
        return sum(nums)

    max_sum = - math.inf
    for i in range(len(nums) - window_size + 1):
        max_sum = max(max_sum, sum(nums[i:i + window_size]))

    return max_sum


if __name__ == '__main__':
    assert solve_method([12, 10, 20, 30, 15, 23], 3) == 68
