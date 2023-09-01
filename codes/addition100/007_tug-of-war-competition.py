#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 007_tug-of-war-competition.py
@time: 2023/9/1 11:37
@project: huawei-od-python
@desc: 007 拔河比赛
"""


def solve_method(arr):
    # 按照身高从高到低、体重从大到小排序
    arr.sort(key=lambda x: (-x[0], -x[1]))
    # 选出10名选手
    return arr[:10]


if __name__ == '__main__':
    arr = [[181, 70], [182, 70], [183, 70], [184, 70], [185, 70],
           [186, 70], [180, 71], [180, 72], [180, 73], [180, 74],
           [180, 75]]
    assert solve_method(arr) == [[186, 70], [185, 70], [184, 70], [183, 70], [182, 70],
                                 [181, 70], [180, 75], [180, 74], [180, 73], [180, 72]]
