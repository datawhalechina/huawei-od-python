#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 282_count-vehicle-colors.py
@time: 2023/7/14 15:31
@project: huawei-od-python
@desc: 282 找出通过车辆最多颜色
"""
import collections


def solve_method(cars: list, time_windows: int):
    max_color = 0
    for i, car in enumerate(cars):
        # 读取窗口中的数据
        if i + 1 >= time_windows:
            count_cars = cars[i + 1 - time_windows: i + 1]
        else:
            count_cars = cars[:i + 1]
        # 使用Counter类构建哈希表
        counter = collections.Counter(count_cars)
        # 得到最多的频数
        max_color = max(max_color, counter.most_common(1)[0][1])

    return max_color


if __name__ == '__main__':
    assert solve_method([0, 1, 2, 1], 3) == 2
    assert solve_method([0, 1, 2, 1], 2) == 1
