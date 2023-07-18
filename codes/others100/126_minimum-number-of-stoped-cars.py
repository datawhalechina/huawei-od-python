#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 126_minimum-number-of-stoped-cars.py
@time: 2023/7/18 15:45
@project: huawei-od-python
@desc: 126 最少停车数
"""


def solve_method(line):
    cars = line.replace(",", "").split("0")
    count = 0
    for car in cars:
        car_len = len(car)
        # 超过3个1，就计算1辆大卡车
        while car_len > 3:
            count += 1
            car_len -= 1
        # 1或2个1，就计算1辆货车或1个小车
        if car_len != 0:
            count += 1
    return count


if __name__ == '__main__':
    assert solve_method("1,0,1") == 2
    assert solve_method("1,1,0,0,1,1,1,0,1") == 3
