#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 015_have-fun.py
@time: 2023/7/13 21:18
@project: huawei-od-python
@desc: 015 开心消消乐
"""


def dfs(n, m, arr, path):
    # 直到列表中的位置都处理完毕，结束
    if len(path) == 0:
        return

    # 开始处理这个位置，从待处理列表中删除这个位置
    node = path.pop(0)
    # 8个方位的相对位置
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    # 将8个方位的1进行反转
    for d in directions:
        new_x = node[0] + d[0]
        new_y = node[1] + d[1]
        if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == 1:
            # 反转为0
            arr[new_x][new_y] = 0
            # 将新位置存放到待处理列表中
            path.append([new_x, new_y])
    # 继续处理列表中的位置，连锁反应
    dfs(n, m, arr, path)


def solve_method(n, m, arr):
    count = 0
    for x in range(n):
        for y in range(m):
            node_value = arr[x][y]
            if node_value == 1:
                # 如果是1，则进行反转
                count += 1
                # 存放待处理位置
                path = [[x, y]]
                # 使用深度优先遍历
                dfs(n, m, arr, path)
    return count


if __name__ == '__main__':
    arr = [[1, 0, 1],
           [0, 1, 0],
           [1, 0, 1]]
    assert solve_method(3, 3, arr) == 1

    arr = [[1, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1]]
    assert solve_method(4, 4, arr) == 2
