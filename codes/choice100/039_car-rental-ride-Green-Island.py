#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 039_car-rental-ride-Green-Island.py
@time: 2023/8/2 9:21
@project: huawei-od-python
@desc: 039 租车骑绿岛
"""


def solve_method(m, arr):
    arr.sort()
    count = 0

    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] <= m:
            i += 1
        j -= 1
        count += 1

    if i == j:
        count += 1

    return count


if __name__ == '__main__':
    assert solve_method(3, [3, 2, 2, 1]) == 3
