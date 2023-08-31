#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 003_the-road-to-work.py
@time: 2023/7/23
@project: huawei-od-python
@desc: 003 上班之路
"""


def dfs(matrix, T, C, i, j, ut, uc, last_dir, path):
    N = len(matrix)
    M = len(matrix[0])
    # 达到目标(公司) return True
    if matrix[i][j] == 'T':
        return True

        # 使用DFS的方式，尝试四个方向 上、下、左、右，i是行，j是列
    for di, dj, direction in [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]:
        # 计算下一个位置的新 行、列值
        new_i, new_j = i + di, j + dj

        # 检查边界以及是否已访问
        if 0 <= new_i < N and 0 <= new_j < M:
            pos = new_i * M + new_j  # 计算新位置的值
            if pos in path:
                continue

            flagT = 0
            # 检查转向次数，如果还有次数可以记录消耗次数
            if last_dir and last_dir != direction:
                if ut + 1 > T: continue
                flagT = 1

            flagC = 0
            # 检查清障次数，如果还有次数可以记录消耗次数
            if matrix[new_i][new_j] == '*':
                if uc + 1 > C: continue
                flagC = 1

            # 添加坐标到访问记录
            path.add(pos)

            # DFS递归，继续走看能否到达 ‘T’
            ut, uc = ut + flagT, uc + flagC
            if dfs(matrix, T, C, new_i, new_j, ut, uc, direction, path):
                return True

            # 回溯移除坐标，减去未成功消耗的次数
            path.remove(pos)
            ut, uc = ut - flagT, uc - flagC

    return False


def solve_method(M, N, T, C, matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'S':
                # 从起点(Jungle的家)开始DFS
                path = set()
                # 使用 i * M + j 来表示具体位置
                path.add(i * M + j)
                return "YES" if dfs(matrix, T, C, i, j, 0, 0, 0, path) else "NO"

    return "NO"


if __name__ == '__main__':
    matrix = ["..S..",
              "****.",
              "T....",
              "****.",
              "....."]
    assert solve_method(5, 5, 2, 0, matrix) == "YES"

    matrix = [".*S*.",
              "*****",
              "..*..",
              "*****",
              "T...."]
    assert solve_method(5, 5, 1, 2, matrix) == "NO"
