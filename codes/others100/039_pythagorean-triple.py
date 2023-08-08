#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 039_pythagorean-triple.py
@time: 2023/8/8 14:34
@project: huawei-od-python
@desc: 勾股数
"""
import math


def solve_method(n, m):
    result = []

    # 判断是否是互质
    def is_coprime(a, b, c):
        return math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1

    # 求勾股数A、B、C
    for a in range(n, m + 1):
        for b in range(a + 1, m + 1):
            # c^2 = i^2+b^2
            c_squared = a ** 2 + b ** 2
            c = int(c_squared ** 0.5)
            if c_squared == c ** 2 and c <= m and is_coprime(a, b, c):
                result.append([a, b, c])

    return result if result else "Na"


if __name__ == '__main__':
    assert solve_method(1, 20) == [[3, 4, 5], [5, 12, 13], [8, 15, 17]]
    assert solve_method(5, 10) == "Na"
