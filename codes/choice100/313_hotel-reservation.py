#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 313_hotel-reservation.py
@time: 2023/8/3 17:43
@project: huawei-od-python
@desc: 313 预订酒店
"""


def solve_method(k, x, prices):
    near_prices = []

    # 计算各个价格与心理价位的距离
    for p in prices:
        near_prices.append((p, abs(p - x)))

    # 按照距离从小到大排序，距离相同时，按照价格从小到大排序
    near_prices.sort(key=lambda x: (x[1], x[0]))

    # 取前k个与心理价位最近的酒店价格
    ans = list(map(lambda x: x[0], near_prices[:k]))
    ans.sort()

    return ans


if __name__ == '__main__':
    assert solve_method(5, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 5, 6, 7, 8]
    assert solve_method(4, 6, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [4, 5, 6, 7]
    assert solve_method(3, 1000, [30, 30, 200, 500, 70, 300]) == [200, 300, 500]
