#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 050_highway-charging-planning.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 050 高速公路充电技术
"""


def solve_method(D, N, sites):
    # 已行驶公里路程
    pos = 0
    # 行驶时间
    driving_time = D // 100
    # 休息时间
    total_rest_time = 0
    while D > 1000:
        # 当前1000公里内的充电站
        _sites = [x for x in sites if pos <= x[0] <= pos + 1000]
        # 将充电站按照充电排队时间从小到大排序
        _sites = sorted(_sites, key=lambda x: x[1])
        # 进站排队充电
        pos, rest_time = _sites[0]
        # 充电时间
        rest_time += 1
        total_rest_time += rest_time
        D -= pos

    total_time = driving_time + total_rest_time
    return total_time


if __name__ == "__main__":
    sites = [[300, 2],
             [600, 1],
             [1000, 0],
             [1200, 0]]
    assert solve_method(1500, 4, sites) == 16

    sites = [[300, 0],
             [600, 0]]
    assert solve_method(800, 2, sites) == 8
