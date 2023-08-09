#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 162_user_scheduling.py
@time: 2023/8/8 21:34
@project: huawei-od-python
@desc: 162 用户调度
"""


def solve_method(n, cost):
    # 构建ABC三个维度的dp表，表示当前选取A或B或C时消耗的最小资源
    dp = [[0,0,0] for i in range(n)]
    # 初始化，因为dp状态转移依赖于前一项
    dp[0] = cost[0]

    for i in range(1, n):
        # 当前选取A时，上一步选取B和C的最小消耗资源
        dp[i][0] = min(dp[i-1][1], dp[i-1][2])+cost[i][0]
        # 当前选取B时，上一步选取A和C的最小消耗资源
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])+cost[i][1]
        # 当前选取C时，上一步选取A和B的最小消耗资源
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])+cost[i][2]
    # 最后一列累加的总和，选取最小值即可
    return min(dp[-1])

if __name__ == '__main__':
    assert solve_method(3, [[15, 8,17],[12, 20, 9],[11, 7, 5]]) == 24
    
