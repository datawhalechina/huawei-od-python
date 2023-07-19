#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 139_witty-delivery-boy.py
@time: 2023/7/19 14:38
@project: huawei-od-python
@desc: 139 机智的外卖员
"""


def solve_method(N, M):
    if N >= M:
        return 0

    dp = [0] * (M + 1)
    # 向下步行需要花费的时间
    for i in range(N + 1):
        dp[i] = N - i
    for i in range(N + 1, M + 1):
        if i % 2 == 0:
            # 从上一层步行到达这一层，耗时+1
            # 坐电梯到达这一层，耗时+1
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            # 从上一层步行到达这一层，耗时+1
            # 乘坐电梯再向下走一层，耗时+2
            dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)

    return dp[M]


if __name__ == '__main__':
    assert solve_method(5, 17) == 4
