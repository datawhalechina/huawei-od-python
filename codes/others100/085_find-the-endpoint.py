#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 085_find-the-endpoint.py
@time: 2023/8/10 14:46
@project: huawei-od-python
@desc: 
"""
import math


def solve_method(nums):
    n = len(nums)
    result = math.inf
    for i in range(1, n // 2):
        # 根据选择的步长，走出第1步
        step = 1
        current_index = i
        while current_index < n:
            # 当走到最后一个位置时，可以比较得到最少步数
            if current_index == n - 1:
                result = min(result, step)
            step += 1
            current_index += nums[current_index]

    return result if result != math.inf else -1


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 7, 1, 5, 9, 3, 2, 1]) == -1
    assert solve_method([7, 5, 9, 4, 2, 7, 1, 1, 1, 1, 1, 1, 1]) == 2
