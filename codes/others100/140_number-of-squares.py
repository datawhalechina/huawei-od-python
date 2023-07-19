#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 140_number-of-squares.py
@time: 2023/7/19 15:21
@project: huawei-od-python
@desc: 140 正方形数量，构成正方形的数量
"""
import itertools
from collections import defaultdict


def check_square(square_points):
    distances = defaultdict(int)
    two_points = itertools.combinations(range(4), 2)
    for two_point in two_points:
        i = two_point[0]
        j = two_point[1]
        x = square_points[i][0] - square_points[j][0]
        y = square_points[i][1] - square_points[j][1]

        distance = x * x + y * y
        distances[distance] += 1

    # 判断4个点组成的距离中，是否存在对角线相等，并且4条边也相等
    return len(distances) == 2 and {2, 4}.issubset(distances.values())


def solve_method(points):
    if len(points) < 4:
        return 0

    count = 0
    # 随机选取4个点，组成一个点阵
    squares = itertools.combinations(range(len(points)), 4)
    for square in squares:
        square_points = [points[square[0]], points[square[1]], points[square[2]], points[square[3]]]
        # 判断这4个点是否能组成一个正方形
        if check_square(square_points):
            count += 1

    return count


if __name__ == '__main__':
    points = [
        [1, 3],
        [2, 4],
        [3, 1]
    ]
    assert solve_method(points) == 0

    points = [
        [0, 0],
        [1, 2],
        [3, 1],
        [2, -1]
    ]
    assert solve_method(points) == 1
