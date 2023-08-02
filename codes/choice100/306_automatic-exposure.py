#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 306_automatic-exposure.py
@time: 2023/8/2 23:47
@project: huawei-od-python
@desc: 306 自动曝光
"""
import math


def solve_method(img):
    img = [min(max(0, x), 255) for x in img]
    avg = sum(img) / 4
    result = 128 - avg
    return math.floor(result)


if __name__ == '__main__':
    assert solve_method([0, 0, 0, 0]) == 128
    assert solve_method([129, 130, 129, 130]) == -2
