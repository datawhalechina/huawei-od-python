#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 033_find-charging-device-combinations.py
@time: 2023/8/1 10:53
@project: huawei-od-python
@desc: 033 查找充电设备组合
"""


def solve_method(P, p_max):
    N = len(P)
    # dp[i][j]表示前i个充电设备中选取功率不超过j的充电设备的最大功率和
    dp = [[0] * (p_max + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(min(P), p_max + 1):
            if P[i - 1] > j:
                # 当前充电设备功率超过了最大功率j，不选择该充电设备
                dp[i][j] = dp[i - 1][j]
            else:
                # 选择该充电设备，选择功率和较大的一个
                dp[i][j] = max(dp[i - 1][j], P[i - 1] + dp[i - 1][j - P[i - 1]])
    return dp[N][p_max]


if __name__ == '__main__':
    assert solve_method([50, 20, 20, 60], 90) == 90
    assert solve_method([50, 40], 30) == 0
