#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 038_hardware-product-sales-plan.py
@time: 2023/8/22 8:56
@project: huawei-od-python
@desc: 038 硬件产品销售方案
"""


def solve_method(amount, prices):
    prices.sort()
    combinations = []
    dfs(prices, amount, 0, [], combinations)
    combinations.sort(key=lambda x: (x[0], -len(x)))
    return combinations


def dfs(prices, amount, index, combination, combinations):
    # 当前amount等于0，说明已经找到了一组解
    if amount == 0:
        combinations.append(combination)
        return
    # 最小的价格大于amount，说明没有解
    if index >= len(prices) or prices[index] > amount:
        return

    for i in range(index, len(prices)):
        if prices[i] <= amount:
            dfs(prices, amount - prices[i], i, combination + [prices[i]], combinations)


if __name__ == "__main__":
    # 500
    # [100, 200, 300, 500]
    # amount = int(input().strip())
    # prices = list(map(int, input().strip('[').strip(']').split(',')))
    # print(solve_method(amount, prices))

    assert sorted(solve_method(500, [100, 200, 300, 500])) == [[100, 100, 100, 100, 100], [100, 100, 100, 200],
                                                               [100, 100, 300], [100, 200, 200], [200, 300], [500]]

    assert sorted(solve_method(100, [100])) == [[100]]
