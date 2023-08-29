#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 160_card-player.py
@time: 2023/8/29 0:21
@project: huawei-od-python
@desc: 160 玩牌高手
"""


def solve_method(scores):
    n = len(scores)
    # dp[i]表示第i轮获得的最大总分数
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 如果当前轮次小于等于3，则总分数置0
        if i <= 3:
            dp[i] = 0
        else:
            # 选择获取该轮牌面分数
            dp[i] = dp[i - 1] + scores[i - 1]
        # 跳过该轮，将当前总分数还原为三轮前的总分数
        dp[i] = max(dp[i], dp[i - 3])

    return dp[n]


if __name__ == '__main__':
    assert solve_method([1, -5, -6, 4, 3, 6, -2]) == 11
