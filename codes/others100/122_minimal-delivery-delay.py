#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 122_minimal-delivery-delay.py
@time: 2023/7/17 20:37
@project: huawei-od-python
@desc: 122 最小传递延时
"""


def backtracking(times, start, end, paths, result):
    if start == end:
        if len(paths) == 1:
            return result.append(paths[0][2])
        elif len(paths) > 1:
            length = 0
            for node in paths:
                length += node[2]
            return result.append(length)

    for node in times:
        if node not in paths:
            if node[0] == start:
                paths.append(node)
                backtracking(times, node[1], end, paths, result)
                paths.remove(node)


def solve_method(times, start, end):
    paths = []
    result = []
    backtracking(times, start, end, paths, result)

    return -1 if len(result) == 0 else min(result)


if __name__ == '__main__':
    times = [[1, 2, 11],
             [2, 3, 13],
             [1, 3, 50]]
    assert solve_method(times, 1, 3) == 24

    times = [[1, 2, 11],
             [2, 3, 13],
             [1, 3, 50],
             [3, 4, 55],
             [4, 5, 35],
             [2, 4, 15],
             [3, 5, 40]]
    assert solve_method(times, 1, 5) == 61
