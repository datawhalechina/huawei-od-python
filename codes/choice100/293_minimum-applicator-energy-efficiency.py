#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 293_minimum-applicator-energy-efficiency.py
@time: 2023/7/31 18:38
@project: huawei-od-python
@desc: 293 最小施肥机能效
"""


def solve_method(n, fields):
    if len(fields) > n:
        return -1

    left = 1
    result = right = max(fields)
    while left <= right:
        m = (left + right) // 2
        # 统计当前效能时，需要的天数
        day = sum(list(map(lambda x: x // m if x % m == 0 else (x // m) + 1, fields)))
        if day <= n:
            right = m - 1
            result = min(result, m)
        else:
            left = m + 1
    return result


if __name__ == '__main__':
    assert solve_method(7, [5, 7, 9, 15, 10]) == 9
    assert solve_method(1, [2, 3, 4]) == -1
