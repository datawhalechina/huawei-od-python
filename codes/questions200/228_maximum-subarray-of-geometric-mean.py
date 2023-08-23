#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 228_maximum-subarray-of-geometric-mean.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 228 几何平均值最大子数组
"""
import math


def calc_geo_mean(numbers):
    value = 1.0
    for num in numbers:
        value *= num
    return math.pow(value, 1.0 / len(numbers))


def solve_method(N, L, nums):
    lo, size = 0, 0
    max_mean = -math.inf
    for i in range(N - L + 1):
        for j in range(i + L, N + 1):
            # 计算子数组的几何平均值
            mean_value = calc_geo_mean(nums[i:j])
            if mean_value - max_mean > 1e-5:
                max_mean = mean_value
                lo = i
                size = j - i
            # 如果几何平均值相差小于等于1e-10，则表示几何平均值相同
            elif mean_value - max_mean <= 1e-10:
                if j - i < size:
                    lo = i
                    size = j - i

    return lo, size


if __name__ == '__main__':
    nums = [2, 2, 3]
    assert solve_method(3, 2, nums) == (1, 2)

    nums = [0.2, 0.1, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2]
    assert solve_method(10, 2, nums) == (2, 2)
