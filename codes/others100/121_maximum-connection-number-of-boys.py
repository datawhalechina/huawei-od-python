#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 121_maximum-connection-number-of-boys.py
@time: 2023/7/17 18:52
@project: huawei-od-python
@desc: 121 最大相连男生数
"""


def dfs(pos, arr, row, column, lenght):
    if not (0 <= row < len(arr) and 0 <= column < len(arr[0])):
        return lenght

    if arr[row][column] == "M":
        lenght += 1

    return dfs(pos, arr, row + pos[0], column + pos[1], lenght)


def solve_method(arr):
    # 表示水平、垂直、对角线或者反对角线方向
    positions = [[0, 1], [1, 0], [1, 1], [-1, -1]]

    max_len = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for pos in positions:
                max_len = max(max_len, dfs(pos, arr, i, j, 0))

    return max_len


if __name__ == '__main__':
    arr = [
        ["F", "M", "M", "F"],
        ["F", "M", "M", "F"],
        ["F", "F", "F", "M"]
    ]
    assert solve_method(arr) == 3
