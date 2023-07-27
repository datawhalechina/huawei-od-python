#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 220_the-number-of-Linux-distributions.py
@time: 2023/7/15
@project: huawei-od-python
@desc: 220 Linux发行版的数量
"""


def dfs(matrix, i, count, visited):
    # 标记节点i已访问
    visited[i] = 1
    # 记录遍历的结点数
    count[0] += 1

    for j in range(len(matrix)):
        # 对邻接矩阵中相连结点做DFS
        if matrix[i][j] == 1 and visited[j] == 0:
            dfs(matrix, j, count, visited)


def solve_method(matrix):
    # 初始化访问数组    
    visited = [0] * len(matrix)
    res = 0

    for i in range(len(matrix)):
        # 发现新连通分量进行DFS 
        if visited[i] == 0:
            count = [0]
            dfs(matrix, i, count, visited)
            # 记录最大结点数
            res = max(res, count[0])

    return res


if __name__ == '__main__':
    matrix = [[1, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 1]]
    assert solve_method(matrix) == 3
