#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 191_calculate-the-nearest-number.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 191 计算最接近的数
"""


def find_median(nums):
    sorted_nums = sorted(nums)
    N = len(sorted_nums)
    return sorted_nums[N // 2]


def solve_method(nums, K):
    # 得到数组的中位数
    mid = find_median(nums)
    min_distance = float('inf')
    index = -1
    for i in range(len(nums) - K + 1):
        # 计算表达式
        count = nums[i]
        for j in range(i + 1, i + K):
            count -= nums[j]

        # 计算与中位数的之差的绝对值
        distance = abs(count - mid)

        # 得到最近的距离和下标
        if distance < min_distance:
            min_distance = distance
            index = i
    return index


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 3], 2) == 2
    assert solve_method([50, 50, 2, 3], 2) == 1
