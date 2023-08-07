#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 033_find-prime-factors.py
@time: 2023/8/7 23:00
@project: huawei-od-python
@desc: 033 分解质因数
"""


def solve_method(num):
    # 找出所有小于num的素数
    tmp = num
    f = 2
    factors = set()
    while tmp != 1:
        if tmp % f != 0:
            f += 1
        else:
            factors.add(f)
            tmp //= f

    # 找出两个素数，满足因数分解
    for f1 in factors:
        for f2 in factors:
            if f1 * f2 == num:
                return min(f1, f2), max(f1, f2)

    return "NO"


if __name__ == '__main__':
    assert solve_method(15) == (3, 5)
    assert solve_method(7) == "NO"
