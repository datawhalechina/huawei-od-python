#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 200_height-and-weight-ordering.py
@time: 2023/8/27 1:33
@project: huawei-od-python
@desc: 200 身高体重排序
"""


def solve_method(n, heights, weights):
    heights = [(i + 1, h) for i, h in enumerate(heights)]
    students = [(h[0], h[1], w) for h, w in zip(heights, weights)]

    # 将身高从低到高、体重从小到大排序
    students.sort(key=lambda x: (x[1], x[2]))

    return "".join([str(x[0]) for x in students])


if __name__ == '__main__':
    assert solve_method(4, [100, 100, 120, 130], [40, 30, 60, 50]) == "2134"
    assert solve_method(3, [90, 110, 90], [45, 60, 45]) == "132"
