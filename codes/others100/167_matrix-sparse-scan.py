#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 167_matrix-sparse-scan.py
@time: 2023/8/8 22:23
@project: huawei-od-python
@desc: 167 矩阵稀疏扫描
"""
# 做法一，模拟
def solve_method1(row, col, matrix):
    count_row = 0
    for i in range(row):
        cnt = matrix[i].count(0)
        if cnt>=col//2:
            count_row+=1
    count_col = 0
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(matrix[j][i])
        cnt = tmp.count(0)
        if cnt>=row//2:
            count_col+=1
    return count_row, count_col

# 做法二，使用numpy并行加速处理
import numpy as np
def solve_menhod2(row, col, matrix):
    

    new_matrix = np.array(matrix)
    cnt_row = cnt_col=0


    # np.count_nonzero(matrix==X)可以统计X数值的个数
    cnt_row = np.count_nonzero(new_matrix==0, axis=1)
    # np.count_nonzero(matrix>=X)可以统计大于等于X数值的个数
    res_row = np.count_nonzero(cnt_row>=col//2)

    cnt_col = np.count_nonzero(new_matrix==0, axis=0)
    res_col = np.count_nonzero(cnt_col>=row//2)

    return res_row, res_col

if __name__ == '__main__':
    assert solve_method1(3, 3, [[1,0,0],[0,1,0],[0,0,1]]) == (3,3)
    assert solve_method1(5,3, [[-1,0,1],[0,0,0],[-1,0,0],[0,-1,0],[0,0,0]]) == (5,3)
    assert solve_method2(3, 3, [[1,0,0],[0,1,0],[0,0,1]]) == (3,3)
    assert solve_method2(5,3, [[-1,0,1],[0,0,0],[-1,0,0],[0,-1,0],[0,0,0]]) == (5,3)
