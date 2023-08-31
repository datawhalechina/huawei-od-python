#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 025_choose-location-of-the-new-school.py
@time: 2023/7/14 20:24
@project: huawei-od-python
@desc: 025 新学校选址
"""


def solve_method(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2 - 1]
    else:
        return arr[len(arr) // 2]


if __name__ == '__main__':
    assert solve_method([0, 20, 40, 10, 30]) == 20
