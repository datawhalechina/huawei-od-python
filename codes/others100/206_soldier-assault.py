#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 206_soldier-assault.py
@time: 2023/7/21 18:05
@project: huawei-od-python
@desc: 206 速战速决、士兵突击
"""
import math


def dfs(x, y, length, direction_index, end_x, end_y, M, N, block, paths, result):
    if x == end_x and y == end_y:
        result = min(result, length)
        return result

    paths.append((x, y))
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    # 各个方向上深度优先搜索
    for i in range(4):
        new_x, new_y = x + directions[i][0], y + directions[i][1]
        if (new_x < 0 or
                new_y < 0 or
                new_x >= M or
                new_y >= N or
                block[new_x][new_y] == "X" or
                (new_x, new_y) in paths):
            continue

        # 士兵每次改变方向时，需要额外花费1个单位的时间
        result = dfs(new_x, new_y, length + int(i != direction_index) + 1, i, end_x, end_y, M, N, block, paths, result)

    return result


def solve_method(block):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for row in range(len(block)):
        for col in range(len(block[0])):
            # 得到起始坐标
            if block[row][col] == "S":
                start_x, start_y = row, col
            # 得到终点坐标
            if block[row][col] == "E":
                end_x, end_y = row, col
    paths = []
    result = math.inf
    M = len(block)
    N = len(block[0])

    result = dfs(start_x, start_y, -1, -1, end_x, end_y, M, N, block, paths, result)

    return result


if __name__ == '__main__':
    block = ["SBBBBB",
             "BXXXXB",
             "BBXBBB",
             "XBBXXB",
             "BXBBXB",
             "BBXBEB"]
    assert solve_method(block) == 13
