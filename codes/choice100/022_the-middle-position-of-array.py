#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 022_the-middle-position-of-array.py
@time: 2023/7/14 17:53
@project: huawei-od-python
@desc: 022 数组的中心位置
"""
from functools import reduce


def solve_method(arr):
    l_prod = 1
    # 初始化右侧乘积，计算数组所有元素乘积
    r_prod = reduce(lambda x, y: x * y, arr)

    for i in range(len(arr)):
        # 逐步剔除左侧元素
        r_prod //= arr[i]
        if l_prod == r_prod:
            return i
        else:
            # 逐步乘以左侧元素
            l_prod *= arr[i]

    return -1


if __name__ == '__main__':
    assert solve_method([2, 5, 3, 6, 5, 6]) == 3
