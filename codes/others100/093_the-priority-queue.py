#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 093_the-priority-queue.py
@time: 2023/8/11 16:46
@project: huawei-od-python
@desc: 093 支持优先级的队列
"""


def solve_method(arr):
    arr = list(set(arr))
    arr.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in arr]


if __name__ == '__main__':
    assert solve_method([(10, 1), (20, 1), (30, 2), (40, 3)]) == [40, 30, 10, 20]
    assert solve_method([(10, 1), (10, 1), (30, 2), (40, 3)]) == [40, 30, 10]
