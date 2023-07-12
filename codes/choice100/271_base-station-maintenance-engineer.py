#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 271_base-station-maintenance-engineer.py
@time: 2023/7/12 15:29
@project: huawei-od-python
@desc: 271 基站维修工程师
"""
import math


def solve_method(num, paths):
    result = []
    backstracking(num, num, 1, [0], result)

    min_path = math.inf
    for path in result:
        total_path = 0
        prev = 0
        for p in path:
            # 计算路径长度
            total_path += paths[prev][p]
            prev = p

        if total_path < min_path:
            min_path = total_path
    return min_path


def backstracking(n, k, start_index, path, result):
    if len(path) == k:
        tmp = path[:]
        tmp.append(0)
        result.append(tmp)
        return

    # 采用放回的取数方式
    for i in set(range(n)).difference(set(path)):
        path.append(i)
        backstracking(n, k, i + 1, path, result)
        path.pop()


if __name__ == '__main__':
    num = 3
    paths_length = [
        [0, 2, 1],
        [1, 0, 2],
        [2, 1, 0],
    ]
    assert solve_method(num, paths_length) == 3
