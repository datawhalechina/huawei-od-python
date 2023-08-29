#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 196_jump-the-grid-1.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 196 跳格子（1）
"""
from collections import defaultdict


def solve_method(n, steps):
    # 格子开启字典，key为前一个格子，value为被开启格子的列表
    step_map = defaultdict(list)
    # 得到没有前置条件的格子
    visited = set(range(n))
    for start, node in steps:
        step_map[start].append(node)
        visited.discard(node)

    while len(step_map) != 0:
        # 如果还有剩余的格子没有开启
        visited_update = set()
        for node in visited:
            nodes = step_map.get(node, [])
            if nodes:
                if not set(nodes).difference(visited):
                    # 如果存在环，则返回no
                    return "no"
                else:
                    # 开启对应的格子
                    visited_update = visited_update.union(set(nodes))
                    step_map.pop(node)
        if visited_update:
            visited = visited.union(visited_update)
        else:
            # 如果无法开启对应的格子，则返回no
            return "no"

    if len(visited) == n:
        return "yes"


if __name__ == '__main__':
    steps = [[0, 1], [0, 2]]
    assert solve_method(3, steps) == "yes"

    steps = [[1, 0], [0, 1]]
    assert solve_method(2, steps) == "no"

    steps = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    assert solve_method(6, steps) == "yes"

    steps = [[4, 3], [0, 4], [2, 1], [3, 2]]
    assert solve_method(5, steps) == "yes"

    steps = [[1, 2], [1, 0]]
    assert solve_method(4, steps) == "yes"

    steps = [[1, 2], [2, 3], [3, 1]]
    assert solve_method(4, steps) == "no"
