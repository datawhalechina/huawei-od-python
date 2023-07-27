#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 241_searching-land-plot-establishment.py
@time: 2023/7/24
@project: huawei-od-python
@desc: 241 探索地块建立
"""


def solve_method(mat, n, m, c, threshold):
    result = 0
    # 遍历矩阵中的每个元素
    for i in range(n - c + 1):
        for j in range(m - c + 1):
            total = 0

            # 计算以该元素为起点的c*c个元素之和
            for k in range(c):
                for l in range(c):
                    total += mat[i + k][j + l]

            # 判断是否超预期
            if total >= threshold:
                result += 1

    return result


if __name__ == '__main__':
    matrix = [[1, 3, 4, 5, 8],
              [2, 3, 6, 7, 1]]

    assert solve_method(matrix, 2, 5, 2, 6) == 4
