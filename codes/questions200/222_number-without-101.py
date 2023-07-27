#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 222_number-without-101.py
@time: 2023/7/23
@project: huawei-od-python
@desc: 222 不含101的数
"""


def solve_method(l, r):
    count = 0
    for i in range(l, r + 1):
        i_bin = bin(i)
        if '101' not in i_bin:
            count += 1

    return count


if __name__ == '__main__':
    assert solve_method(1, 10) == 8
    assert solve_method(10, 20) == 7
