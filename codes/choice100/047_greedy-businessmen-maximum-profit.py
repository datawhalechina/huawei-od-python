#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 047_greedy-businessmen-maximum-profit.py
@time: 2023/8/3 16:04
@project: huawei-od-python
@desc: 047 贪心的商人、最大利润
"""


def max_profit(prices) -> int:
    length = len(prices)
    # dp[i][0] 表示第i天持有商品所得现金。
    # dp[i][1] 表示第i天不持有商品所得最多现金
    dp = [[0] * 2 for _ in range(length)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    for i in range(1, length):
        # 第i天持有商品所得现金=第i-1天持有商品与第i天买入商品的最大值
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        # 第i天不持有商品所得最多现金=第i-1天不持有商品和第i天卖出商品的最大值
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    return dp[-1][1]


def solve_method(number, days, item, item_price):
    """
    :param number: 商品种类数量
    :param days: 天数
    :param item: 每种商品的个数
    :param item_price: 每种商品每天的价格
    :return: 最大利润
    """

    ans = 0
    for i in range(number):
        # 该种商品每天的价格
        prices = item_price[i]
        ans += max_profit(prices) * item[i]
    return ans


if __name__ == '__main__':
    item_price = [[1, 2, 3],
                  [4, 3, 2],
                  [1, 5, 2]]
    assert solve_method(3, 3, [4, 5, 6], item_price) == 32
    assert solve_method(1, 1, [1], [[1]]) == 0
