#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 201_interscholasticmeet.py
@time: 2023/7/20 15:21
@project: huawei-od-python
@desc: 201 运动会
"""


def solve_method(n, heights, weights):
    result = []
    for i in range(n):
        # 使用元组存储数据
        result.append((i + 1, heights[i], weights[i]))
    result.sort(key=lambda x: (x[1], x[2]))

    return [x[0] for x in result]


if __name__ == "__main__":
    heights = [100, 100, 120, 130]
    weights = [40, 30, 60, 50]
    assert solve_method(4, heights, weights) == [2, 1, 3, 4]

    heights = [90, 110, 90]
    weights = [45, 60, 45]
    assert solve_method(3, heights, weights) == [1, 3, 2]
