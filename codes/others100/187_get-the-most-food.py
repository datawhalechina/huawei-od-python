#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 187_get-the-most-food.py
@time: 2023/8/27 1:30
@project: huawei-od-python
@desc: 187 获取最多食物
"""
import math


def solve_method(grids):
    def dfs(n_id):
        nonlocal dp
        if n_id not in dp:
            if nodes[n_id][0] == -1:
                dp[n_id] = nodes[n_id][1]
            else:
                dp[n_id] = max(nodes[n_id][1], nodes[n_id][1] + dfs(nodes[n_id][0]))
        return dp[n_id]

    n = len(grids)
    # 方格id字典，key为方格id，value为能传送的方格id和食物。
    nodes = {}
    for i in range(n):
        node_id, pid, val = grids[i]
        if node_id < 0 or node_id >= n or pid < -1 or pid >= n:
            continue
        nodes[node_id] = [pid, val]

    max_val = -math.inf
    # dp[i]表示到达该点能获得的最大食物
    dp = {}
    for i in reversed(range(n)):
        if i not in nodes:
            continue
        max_val = max(max_val, dfs(i))

    return max_val


if __name__ == '__main__':
    arr = [[0, 1, 8],
           [1, -1, -2],
           [2, 1, 9],
           [4, 0, -2],
           [5, 4, 3],
           [3, 0, -3],
           [6, 2, -3]]
    assert solve_method(arr) == 9

    arr = [[0, -1, 3],
           [1, 0, 1],
           [2, 0, 2]]
    assert solve_method(arr) == 5
