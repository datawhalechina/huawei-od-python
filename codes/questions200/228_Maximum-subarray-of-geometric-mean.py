#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 228_Maximum-subarray-of-geometric-mean.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 228 
"""
import math

def calc_mean(numbers):
    value = 1.0
    for num in numbers:
        value *= num
    return math.pow(value, 1.0 / len(numbers))

def solve_method(N, L, numbers):
    lo, size = 0, 0
    max_mean = float("-inf")
    for i in range(N - L + 1):
        for j in range(i + L, N + 1):
            # 计算子数组的几何平均值
            mean_value = calc_mean(numbers[i:j])
            if mean_value - max_mean > 1e-5:
                max_mean = mean_value
                lo = i
                size = j - i
            # 题目用例保证几何平均值相差小于等于 1e-10 即为相同
            elif mean_value - max_mean <= 1e-10:
                if j - i < size:
                    lo = i
                    size = j - i

    return (lo, size)

if __name__ == '__main__':
    numbers = [2, 2, 3]
    assert solve_method(3, 2, numbers) == (1, 2)

    numbers = [0.2, 0.1, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2]
    assert solve_method(10, 2, numbers) == (2, 2)