#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 066_find-path
@time:  14/8/2023 下午 2:51
@project:  huawei-od-python 
"""
import math


def solve_method(nums):
    depth = math.ceil(math.log2(len(nums)))  # nums第一个元素无意义，为额外添加元素，目的是对齐下标
    start = 2 ** (depth - 1)
    min_value, index = float('inf'), -1
    for i in range(start, len(nums)):
        if nums[i] != -1 and nums[i] < min_value:
            min_value, index = nums[i], i
    path = []
    while index > 0:
        path.append(nums[index])
        index = index // 2
    return path[::-1]


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(' ')))
    nums.insert(0, 0)
    res = solve_method(nums)
    print(res)
