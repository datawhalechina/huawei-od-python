#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 032_sharing-apples.py
@time: 2023/8/7 22:56
@project: huawei-od-python
@desc: 032 分苹果
"""


def solve_method(apples):
    count = 0
    for i in apples:
        # 进行异或运算，等同于不进位的加法
        count = count ^ i
    if count == 0:
        return sum(apples) - min(apples)
    else:
        return -1


if __name__ == '__main__':
    assert solve_method([3, 5, 6]) == 11
    assert solve_method([7258, 6579, 2602, 6716, 3050, 3564, 5396, 1773]) == 35165
