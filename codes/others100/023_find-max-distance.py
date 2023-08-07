#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 023_find-max-distance.py
@time: 2023/8/7 13:53
@project: huawei-od-python
@desc: 023 停车场最大的距离
"""


def solve_method(sites):
    # 初始化最大距离为0
    max_distance = 0

    for i, n in enumerate(sites):
        if n == 0:
            # 计算该空车位与最近的已停车车辆之间的距离
            distance = min([abs(i - j) for j, x in enumerate(sites) if x == 1])
            # 获取最大距离
            if distance > max_distance:
                max_distance = distance

    return max_distance


if __name__ == '__main__':
    sites = [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    assert solve_method(sites) == 2
