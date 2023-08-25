#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 064_find-max-value
@time:  2023/8/17 11:44
@project:  huawei-od-python
@desc: 064 寻找最大价值的矿堆
"""


def solve_method(nums):
    m, n = len(nums), len(nums[0])
    if m < 1:
        return 0

    def dfs(row, col):
        nonlocal value
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or nums[row][col] == 0 or nums[row][col] == -1:
            # 如果超出边界或者已经访问过（标记为-1），则返回0
            return 0
        else:
            value = nums[row][col]
            # 已经访问过，标记为-1
            nums[row][col] = -1
            for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                # 上下左右进行深度优先搜索
                value += dfs(row + d1, col + d2)
            return value

    max_value = -1
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1 or nums[i][j] == 2:
                value = dfs(i, j)
                if value > max_value:
                    max_value = value
    return max_value


if __name__ == '__main__':
    arr = [[2, 2, 2, 2, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1]]
    assert solve_method(arr) == 8

    arr = [[2, 2, 2, 2, 0],
           [0, 0, 0, 2, 0],
           [0, 0, 0, 1, 0],
           [0, 1, 1, 1, 1]]
    assert solve_method(arr) == 15
