#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 194_street-lighting.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 194 路灯照明
"""


def solve_method(nums):
    prev = nums[0]
    result = 0
    for i in range(1, len(nums)):
        if prev + nums[i] < 100:
            result += 100 - (prev + nums[i])
        prev = nums[i]

    return result


if __name__ == '__main__':
    assert solve_method([50, 50]) == 0
    assert solve_method([50, 40]) == 10
    assert solve_method([50, 40, 30, 20, 10]) == 160
