#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 124_minimum-number-of-steps.py
@time: 2023/7/18 14:11
@project: huawei-od-python
@desc: 124 最小步骤数
"""
import math


def solve_method(nums):
    min_step = math.inf
    n = len(nums)
    for i in range(1, n // 2):
        step = 1
        index = i

        while True:
            # 以所在元素的数字走相应的步数
            index += nums[index]
            step += 1
            if index > n - 1:
                break
            elif index == n - 1:
                min_step = min(min_step, step)
                break

    return -1 if min_step == math.inf else min_step


if __name__ == '__main__':
    assert solve_method([7, 5, 9, 4, 2, 6, 8, 3, 5, 4, 3, 9]) == 2
    assert solve_method([1, 2, 3, 7, 1, 5, 9, 3, 2, 1]) == -1
