#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 138_robots-walk-mazes.py
@time: 2023/7/19 13:33
@project: huawei-od-python
@desc: 138 机器人走迷宫
"""


def dfs(x, y, X, Y, dp):
    if x == X - 1 and y == Y - 1:
        # 出口
        dp[x][y] = 1
        return 1
    elif x >= X or y >= Y or dp[x][y] == 0:
        # 墙壁
        return "A"
    elif dp[x][y] != "B":
        # 不是陷阱
        return dp[x][y]
    else:
        # 递归遍历得到向上和向右的方格情况
        up = dfs(x + 1, y, X, Y, dp)
        right = dfs(x, y + 1, X, Y, dp)
        if up == "A" and right == "A":
            # 两个位置的方格都不可达，则此方格不可达
            dp[x][y] = "A"
        elif right == 1 or up == 1:
            # 如果有一个位置的方格可以走，则此方格可以走
            dp[x][y] = 1
        return dp[x][y]


def solve_method(X, Y, obstacles):
    dp = [["B"] * Y for _ in range(X)]

    for obstacle in obstacles:
        i, j = obstacle[0], obstacle[1]
        dp[i][j] = 0

    dfs(0, 0, X, Y, dp)

    # 陷阱方格
    B_cells = sum(row.count("A") for row in dp)
    # 不可达方格
    A_cells = sum(row.count("B") for row in dp)

    return B_cells, A_cells


if __name__ == '__main__':
    obstacles = [
        [0, 2],
        [1, 2],
        [2, 2],
        [4, 1],
        [5, 1]
    ]
    assert solve_method(6, 4, obstacles) == (2, 3)

    obstacles = [
        [2, 0],
        [2, 1],
        [3, 0],
        [3, 1]
    ]
    assert solve_method(6, 4, obstacles) == (0, 4)
