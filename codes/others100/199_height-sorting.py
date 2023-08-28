#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 199_height-sorting.py
@time: 2023/8/27 1:33
@project: huawei-od-python
@desc: 199 身高排序
"""


def solve_method(H, N, heights):
    heights.sort(key=lambda x: (abs(x - H), x))
    return heights


if __name__ == '__main__':
    heights = [95, 96, 97, 98, 99, 101, 102, 103, 104, 105]
    assert solve_method(100, 10, heights) == [99, 101, 98, 102, 97, 103, 96, 104, 95, 105]
