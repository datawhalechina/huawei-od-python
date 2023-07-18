#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 129_the-nearest-point.py
@time: 2023/7/18 19:10
@project: huawei-od-python
@desc: 129 最近的点
"""


def solve_method(setA, setB, R):
    result = []
    for a in setA:
        for b in setB:
            if a <= b and b - a <= R:
                result.append([a, b])
                setB.remove(b)
                break

    return result


if __name__ == '__main__':
    setA = [1, 5, 5, 10]
    setB = [1, 3, 8, 8, 20]
    R = 5
    assert solve_method(setA, setB, R) == [[1, 1], [5, 8], [5, 8]]
