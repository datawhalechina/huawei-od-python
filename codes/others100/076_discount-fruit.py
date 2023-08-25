#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 076_discount-fruit
@time:  2023/7/30 22:41
@project:  huawei-od-python
@desc: 076 打折买水果
"""
from collections import defaultdict


def solve_method(n, hour_prices):
    """
    :param n: 总小时数
    :param hour_prices: 不同时间段提供不同价格的打折水果的价格
    :return: 采购水果的最便宜的花费总和
    """
    hour_price_dict = defaultdict(list)

    # 构建时刻价格字典，key为时刻，value为水果价格列表
    for start_time, end_time, price in hour_prices:
        for x in range(start_time, end_time + 1):
            hour_price_dict[x].append(price)

    total_cost = 0
    for i in range(n):
        total_cost += min(hour_price_dict[i+1])

    return total_cost


if __name__ == '__main__':
    hour_prices = [[2, 3, 10],
                   [2, 4, 20],
                   [1, 3, 15],
                   [1, 4, 25],
                   [3, 4, 8],
                   [1, 4, 16]]
    assert solve_method(4, hour_prices) == 41

    hour_prices = [[1, 2, 30],
                   [1, 5, 20],
                   [3, 5, 10]]
    assert solve_method(5, hour_prices) == 70
