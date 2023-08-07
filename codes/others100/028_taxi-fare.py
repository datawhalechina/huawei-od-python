#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 028_taxi-fare.py
@time: 2023/8/7 18:10
@project: huawei-od-python
@desc: 028 出租车计费
"""


def solve_method(num):
    real = 0
    count = 0
    while num > 0:
        n = num % 10
        # 大于4的情况
        if n > 4:
            n = n - 1
        real = real + n * 9 ** count
        count = count + 1
        num = num // 10
    return real


if __name__ == '__main__':
    assert solve_method(5) == 4
    assert solve_method(17) == 15
    assert solve_method(100) == 81
