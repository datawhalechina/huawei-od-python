#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 248_min-number-of-segments-covered.py
@time: 2023/8/21 11:30
@project: huawei-od-python
@desc: 248 最少数量线段覆盖
"""
from collections import defaultdict


def solve_method(n, points):
    # line_dict存储整数点和出现的次数
    line_dict = defaultdict(int)
    for point in points:
        for i in range(point[0], point[1] + 1):
            line_dict[i] += 1
    # del_count记录可删除的线段数
    del_count = 0
    for point in points:
        # 如果若线段上每个点出现次数均大于1，则可以删除该线段
        if all([True if line_dict[i] > 1 else False for i in range(point[0], point[1] + 1)]):
            for i in range(point[0], point[1] + 1):
                line_dict[i] -= 1
            del_count += 1
    return n - del_count


if __name__ == "__main__":
    # n = int(input())
    # points = []
    # for _ in range(n):
    #     x, y = map(int, input().split(','))
    #     points.append((x, y))
    # print(solve_method(n, points))

    assert solve_method(3, [[1, 4], [2, 5], [3, 6]]) == 2
