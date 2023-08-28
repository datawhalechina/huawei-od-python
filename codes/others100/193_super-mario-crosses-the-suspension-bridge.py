#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 193_super-mario-crosses-the-suspension-bridge.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 193 超级玛丽过吊桥
"""


def solve_method(M, N, K, L):
    """
    :param M: 超级玛丽当前的生命数
    :param N: 吊桥的长度
    :param K: 缺失木板数
    :param L: 缺失木板编号数组
    :return: 通过此关的吊桥走法个数
    """
    bridge = [True] * (N + 2)
    for i in L:
        bridge[i] = False

    # dp[i][j]表示达到位置i并剩余j条生命的方法数
    dp = [[0] * (M + 2) for _ in range(N + 2)]
    # 表示从起点出发，剩余M条生命的方案数为1
    dp[0][M] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0]) - 1):
            k = j + 1 if not bridge[i] else j
            if i == 1:
                dp[i][j] = dp[i - 1][k]
            elif i == 2:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k]
            else:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k] + dp[i - 3][k]
    res = sum(dp[N + 1][: len(dp[0]) - 1])
    return res


if __name__ == "__main__":
    assert solve_method(2, 2, 1, [2]) == 4
    assert solve_method(1, 3, 2, [1, 3]) == 1
