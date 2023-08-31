#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 037_wolf-sheep-crossing-the-river.py
@time: 2023/8/21 20:14
@project: huawei-od-python
@desc: 037 狼羊过河、羊狼农夫过河
"""


def solve_method(m, n, x):
    # min_count为最小运输次数
    global min_count
    min_count = (m + n) * x
    dfs(m, n, 0, 0, x, 0)
    return 0 if min_count == (m + n) * x else min_count


def dfs(m0, n0, m1, n1, x, count):
    """
    :param m0: 剩余的羊的数量
    :param n0: 剩余的狼的数量
    :param m1: 运送到对岸的羊的数量
    :param n1: 运送到对岸的狼的数量
    :param x: 船的容量
    :param count: 运输次数
    """
    # 终止条件：全部运到对岸
    global min_count
    if m0 == 0 and n0 == 0:
        min_count = min(min_count, count)
        return

    # 尝试运输i只羊和j只狼
    for i in range(min(m0 + 1, x + 1)):
        for j in range(min(n0 + 1, x + 1)):
            # 不必运输0只羊和0只狼
            if i == 0 and j == 0:
                continue
            # 狼羊的总数不能超出船的容量
            if i + j > x:
                break
            # 离岸时检查两侧的狼羊数量
            if (m0 - i > n0 - j or m0 - i == 0) and (m1 + i > n1 + j or m1 + i == 0):
                dfs(m0 - i, n0 - j, m1 + i, n1 + j, x, count + 1)


if __name__ == "__main__":
    # m只羊，n只狼，x为船容量
    # m, n, x = map(int, input().split())
    # print(solve_method(m, n, x))

    assert solve_method(5, 3, 3) == 3
