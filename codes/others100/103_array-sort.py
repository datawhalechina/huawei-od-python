#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 103_array-sort.py
@time: 2023/7/25 21:15
@project: huawei-od-python
@desc: 103 数组排序
"""
from collections import defaultdict


def solve_method(nums):
    # key为数字，value为(位置, 个数)
    num_dict = {}
    for i, num in enumerate(nums):
        if num not in num_dict:
            num_dict[num] = (i, 1)
        else:
            count = num_dict[num][1] + 1
            num_dict[num] = (num_dict[num][0], count)

    result = sorted(num_dict.items(), key=lambda x: (-x[1][1], x[1][0]))
    return [x[0] for x in result]


if __name__ == '__main__':
    assert solve_method([1, 3, 3, 3, 2, 4, 4, 4, 5]) == [3, 4, 1, 2, 5]
