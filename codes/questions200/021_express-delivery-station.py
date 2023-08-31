#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 021_express-delivery-station.py
@time: 2023/7/24
@project: huawei-od-python
@desc: 021 快递业务站
"""


def solve_method(N, stations_relations):
    cover = set()
    res = 0

    for i in range(N):
        if i not in cover:
            res += 1
            cover.add(i)
        for j in filter(lambda x: x != i, range(N)):
            if stations_relations[i][j] == 1:
                cover.add(j)

    return res


if __name__ == '__main__':
    stations_relations = [
        [1, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
    ]

    assert solve_method(4, stations_relations) == 1

    stations_relations = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

    assert solve_method(4, stations_relations) == 3
