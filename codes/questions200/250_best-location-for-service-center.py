#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 250_best-location-for-service-center.py
@time: 2023/8/21 16:23
@project: huawei-od-python
@desc: 250 服务中心选址、服务中心的最佳位置
"""


def solve_method(n, positions):
    positions.sort(key=lambda x: (x[0], x[1]))

    left = positions[0][0]
    right = positions[-1][1]
    while left < right:
        mid = (right + left) // 2
        if get_distance(mid, positions) < get_distance(mid + 1, positions):
            right = mid
        else:
            left = mid + 1
    return get_distance(left, positions)


def get_distance(location, positions):
    distance = 0
    for position in positions:
        if position[0] > location:
            distance += position[0] - location
        elif position[1] < location:
            distance += location - position[1]
    return distance


if __name__ == "__main__":
    # 3
    # 1 2
    # 3 4
    # 10 20
    # n = int(input())
    # positions = []
    # for _ in range(n):
    #     positions.append(list(map(int, input().split())))
    # print(solve_method(n, positions))

    assert solve_method(3, [[1, 2], [3, 4], [10, 20]]) == 8
    assert solve_method(2, [[1, 4], [4, 5]]) == 0
    assert solve_method(4, [[1, 3], [2, 6], [8, 10], [15, 18]]) == 14
