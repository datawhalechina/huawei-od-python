#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 227_signal-transmission-and-reception.py
@time: 2023/8/17
@project: huawei-od-python
@desc: 227 信号发射和接收
"""


def can_receive(ant_heights):
    # 如果相邻，一定能接收到信号
    if len(ant_heights) == 2:
        return True

    start_ant = ant_heights[0]
    end_ant = ant_heights[len(ant_heights) - 1]
    next_ant_idx = 1
    temp_height = 0

    # 判断中间是否有阻碍
    while next_ant_idx < len(ant_heights) - 1:
        next_ant = ant_heights[next_ant_idx]
        # 如果起始天线矮于下一个天线，则无法接收到
        if start_ant <= next_ant:
            return False

        temp_height = max(temp_height, next_ant)
        # 如果中间最高的天线高于终点天线，则无法接收到
        if temp_height >= end_ant:
            return False

        next_ant_idx += 1

    return True


def solve_method(rows: int, cols: int, ant_heights: list[list[int]]):
    ret = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i != rows - 1:
                k = i + 1
                ant_cols = [row[j] for row in ant_heights]
                # 遍历南向的后续天线，判断是否能接收到当前天线的信号
                while k < rows:
                    if can_receive(ant_cols[i: k + 1]):
                        ret[k][j] += 1
                    k += 1
            if j != cols - 1:
                k = j + 1
                # 遍历东向的后续天线，判断是否能接收到当前天线的信号
                while k < cols:
                    if can_receive(ant_heights[i][j: k + 1]):
                        ret[i][k] += 1
                    k += 1

    return rows, cols, ret


if __name__ == '__main__':
    heights = [[2, 4, 1, 5, 3, 3]]
    output = [[0, 1, 1, 2, 1, 1]]
    assert solve_method(1, 6, heights) == (1, 6, output)

    heights = [[2, 5, 4, 3, 2, 8], [9, 7, 5, 10, 10, 3]]
    output = [[0, 1, 1, 1, 1, 4], [1, 2, 2, 4, 2, 2]]
    assert solve_method(2, 6, heights) == (2, 6, output)
