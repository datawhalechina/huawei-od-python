#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 016_sites-with-the-most-people.py
@time: 2023/7/26 20:58
@project: huawei-od-python
@desc: 016 人数最多的站点
"""
from collections import defaultdict


def solve_method(people):
    station_people = defaultdict(int)
    for p in people:
        for station in range(p[0], p[1] + 1):
            station_people[station] += 1

    result = sorted(station_people.items(), key=lambda x: -x[1])
    return result[0][0]


if __name__ == '__main__':
    people = [(1, 3), (2, 4), (1, 4)]
    assert solve_method(people) == 2
