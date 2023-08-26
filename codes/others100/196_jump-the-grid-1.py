#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 196_jump-the-grid-1.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 196 跳格子（1）
"""

from typing import List


def skip_grid(n: int, grids: List[List[int]]) -> bool:
    x = [None] * n
    map = {}
    for i in range(len(grids)):
        a = grids[i]
        if a[0] not in map:
            map[a[0]] = []
        map[a[0]].append(a[1])
        x[a[1]] = a[0]
    stack = []
    for i in range(n):
        if x[i] is None:
            stack.append(i)
    if not stack:
        return False
    while stack:
        index = stack.pop()
        x[index] = -1
        if index not in map:
            continue
        for item in map[index]:
            if x[item] != -1:
                stack.append(item)
    return all(val == -1 for val in x)


if __name__ == '__main__':
    n = 2
    grids = [[1, 0], [0, 1]]
    r = skip_grid(n, grids)
    print("yes" if r else "no")
