#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 128_the-nearest-hospital.py
@time: 2023/7/18 18:48
@project: huawei-od-python
@desc: 128 最近的医院
"""


def solve_method(x, y, m, l, n):
    tA = l + (x * 1000 / m)
    tB = y * 1000 / n

    if tA < tB:
        return "Taxi"
    elif tA > tB:
        return "Walk"
    else:
        return "Same"


if __name__ == '__main__':
    assert solve_method(50, 5, 500, 30, 90) == "Walk"
