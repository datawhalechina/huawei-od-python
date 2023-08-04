#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 120_maximum-return-stock-return-problem.py
@time: 2023-07-30 18:42:56
@project: huawei-od-python
@desc: 120 最大收益股票收益问题
"""


def convert_yuan(price: str):
    value = int(price[:-1])
    if price.endswith("S"):
        value *= 7
    return value


def solve_method(prices):
    prices = list(map(convert_yuan, prices))

    length = len(prices)
    # dp[i][0] 表示第i天持有股票所得现金。
    # dp[i][1] 表示第i天不持有股票所得最多现金
    dp = [[0] * 2 for _ in range(length)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    for i in range(1, length):
        # 第i天持有股票所得现金=第i-1天持有股票与第i天买入股票的最大值
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        # 第i天不持有股票所得最多现金=第i-1天不持有股票和第i天卖出股票的最大值
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    return dp[-1][1]


if __name__ == '__main__':
    assert solve_method(["2Y", "3S", "4S", "6Y", "8S"]) == 76
