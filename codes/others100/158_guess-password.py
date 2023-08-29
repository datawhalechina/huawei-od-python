#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 158_guess-password.py
@time: 2023/8/29 0:20
@project: huawei-od-python
@desc: 158 猜密码
"""
from itertools import combinations


def solve_method(nums, k):
    # 生成所有可能的组合
    combinations_list = []
    for length in range(k, len(nums) + 1):
        combinations_list.extend(combinations(nums, length))

    # 按照要求进行排序
    combinations_list.sort()

    return [list(x) for x in combinations_list ]


if __name__ == '__main__':
    assert solve_method([2, 3, 4], 2) == [[2, 3], [2, 3, 4], [2, 4], [3, 4]]
