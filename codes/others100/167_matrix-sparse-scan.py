#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 167_matrix-sparse-scan.py
@time: 2023/8/8 22:23
@project: huawei-od-python
@desc: 167 矩阵稀疏扫描
"""


def solve_method1(row, col, matrix):
    count_row = 0
    required_zeros = col // 2
    for i in range(row):
        cnt = matrix[i].count(0)
        if cnt >= required_zeros:
            count_row += 1

    count_col = 0
    required_zeros = row // 2
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(matrix[j][i])
        cnt = tmp.count(0)
        if cnt >= required_zeros:
            count_col += 1
    return count_row, count_col


if __name__ == '__main__':
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert solve_method1(3, 3, matrix) == (3, 3)
    matrix = [[-1, 0, 1], [0, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 0]]
    assert solve_method1(5, 3, matrix) == (5, 3)
