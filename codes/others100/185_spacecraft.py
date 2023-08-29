#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 185_spacecraft.py
@time: 2023/8/27 1:29
@project: huawei-od-python
@desc: 185 航天器
"""


def solve_method(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            area = min(nums[i], nums[j]) * (j - i)
            result = max(result, area)

    return result


if __name__ == '__main__':
    assert solve_method([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
