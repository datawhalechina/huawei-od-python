#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 013_queuing-games.py
@time: 2023/9/1 18:25
@project: huawei-od-python
@desc: 013 排队游戏
"""


def solve_method(k, prickers_pos, students):
    satisfied_value = 0

    for i in range(len(students)):
        if i not in prickers_pos:
            satisfied_value += sum([1 for j in range(0, i) if students[j] > students[i]])

    if satisfied_value > k:
        return 1
    return 0


if __name__ == '__main__':
    prickers_pos = [0, 1]
    students = [1810, 1809, 1801, 1802]
    assert solve_method(3, prickers_pos, students) == 1
