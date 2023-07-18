#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 123_minimum-leaf-node.py
@time: 2023/7/18 13:35
@project: huawei-od-python
@desc: 123 最小叶子节点
"""
import math


def backtracking(arr, min_pos, paths):
    paths.append(arr[min_pos])
    if min_pos == 1:
        return
    if min_pos % 2 == 0:
        # 该节点是上一个节点的左子节点
        backtracking(arr, min_pos // 2, paths)
    else:
        # 该节点是上一个节点的右子节点
        backtracking(arr, (min_pos - 1) // 2, paths)


def solve_method(arr):
    # 插入头节点
    arr.insert(0, 0)

    # 找到最小值，即最小叶子节点
    min_val = math.inf
    min_pos = 0
    for i in range(2, len(arr)):
        val = arr[i]
        if val not in [0, -1] and val < min_val and i * 2 > len(arr):
            min_val = val
            min_pos = i
    # 回溯，找到路径
    paths = []
    backtracking(arr, min_pos, paths)
    paths.reverse()
    return paths


if __name__ == '__main__':
    assert solve_method([3, 5, 7, -1, -1, 2, 4]) == [3, 7, 2]
    assert solve_method([5, 9, 8, -1, -1, 7, -1, -1, -1, -1, -1, 6]) == [5, 8, 7, 6]
