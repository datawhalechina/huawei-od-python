#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 005_n-decimal-subtraction.py
@time: 2023/7/26 10:35
@project: huawei-od-python
@desc: 005 N进制减法
"""


def to_str(num, base):
    base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXY"
    if num < base:
        return base_str[num]
    else:
        return to_str(num // base, base) + base_str[num % base]


def solve_method(N, a, b):
    if N < 2 or N > 35:
        return "-1", "ERROR"

    diff = int(a, N) - int(b, N)
    sign = 0 if diff >= 0 else 1
    return sign, to_str(diff, N)


if __name__ == '__main__':
    assert solve_method(2, "11", "1") == (0, "10")
