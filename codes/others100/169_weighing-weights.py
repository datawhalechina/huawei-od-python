#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 169_weighing-weights.py
@time: 2023/8/8 22:36
@project: huawei-od-python
@desc: 169 称砝码
"""


def solve_method(n, weights, nums):
    new_weights = []
    for i in range(n):
        new_weights.extend([weights[i]]*nums[i])
    # dp 数组中的元素表示能否使用给定的砝码组成对应的重量，而不是最大价值。
    # 默认重量为0也是一种，则初始化dp[0]=True。
    total_weight = sum(new_weights)
    dp = [False]*(total_weight+1)
    dp[0]=True
    for w in new_weights:
        for j in reversed(range(w, total_weight+1)):
            dp[j] = dp[j] or dp[j-w]
            # 标准01背包状态转移方程，求装满j的最大重量
            # dp[j] = max(dp[j], dp[j-w]+w)
    return sum(dp)


if __name__ == '__main__':
    assert solve_method(2, [1,2],[2,1]) == 5
