#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 118_the-largest-submatrix.py
@time: 2023-07-29 16:16:19
@project: huawei-od-python
@desc: 118 最大子矩阵
"""


def solve_method(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    # 遍历所有可能的上边界
    for top in range(rows):
        # 初始化dp数组，用于保存每列的累计和
        dp = [0] * cols

        # 遍历所有可能的下边界
        for bottom in range(top, rows):
            # 更新dp数组，计算每列的累计和
            for i in range(cols):
                dp[i] += matrix[bottom][i]

            # 使用Kadane's算法计算dp数组的最大子数组和
            current_sum = 0
            max_temp = float('-inf')
            for i in range(cols):
                current_sum = max(dp[i], current_sum + dp[i])
                max_temp = max(max_temp, current_sum)

            # 更新最大子矩阵和
            max_sum = max(max_sum, max_temp)

    return max_sum


if __name__ == '__main__':
    assert solve_method([[-3, 5, -1, 5], [2, 4, -2, 4], [-1, 3, -1, 3]]) == 20
    assert solve_method([[-3, 50, -10, -5], [-2, -4, -2, -4], [-1, -3, -1, -3]]) == 50
