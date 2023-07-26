#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 013_event-push.py
@time: 2023/7/26 19:44
@project: huawei-od-python
@desc: 013 事件推送
"""


def solve_method(A, B, R):
    result = []
    index = 0
    for a in A:
        while index < len(B):
            if a <= B[index] and B[index] - a <= R:
                result.append([a, B[index]])
                break
            index += 1

    return result


if __name__ == '__main__':
    A = [1, 5, 5, 10]
    B = [1, 3, 8, 8, 20]
    assert solve_method(A, B, 5) == [[1, 1], [5, 8], [5, 8]]
