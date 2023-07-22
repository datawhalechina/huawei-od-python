#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 213_the-number-of-unbroadcast-servers.py
@time: 2023/7/22 22:17
@project: huawei-od-python
@desc: 213 需要广播的服务器数量
"""
from collections import defaultdict


def solve_method(arr):
    # 连接关系
    connect_map = defaultdict(list)
    for i in range(len(arr)):
        is_contain = False
        # 寻找是否与该服务器相连的服务器
        for k, v in connect_map.items():
            if i in v:
                is_contain = True
                map_key = k
        # 如果没有，则初始化连接关系
        if not is_contain:
            connect_map[i] = []
            map_key = i
        # 继续寻找后续服务器是否与该服务器直接连接
        for j in range(i, len(arr)):
            if i != j and arr[i][j] == 1:
                # 如果有直接连接的服务器，则放入对应的列表中
                connect_map[map_key].append(j)

    # 得到需要广播的服务器数量，即为相连关系中的服务器个数。
    return len(connect_map)


if __name__ == '__main__':
    arr = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    assert solve_method(arr) == 3

    arr = [[1, 1],
           [1, 1]]
    assert solve_method(arr) == 1

    arr = [[1, 1, 0],
           [1, 1, 0],
           [0, 0, 1]]
    assert solve_method(arr) == 2
