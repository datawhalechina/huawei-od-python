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

    # dp[i][j]表示走到第i个位置时，此时生命值为j时的走法数
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 2)]
    # 当在初始位置时，生命值为M，走法数为1
    dp[0][M] = 1

    # 遍历每一个位置
    for i in range(1, N + 2):
        # 寻找生命值从0到M的走法
        for j in range(M + 1):
            # 如果遇到陷阱，（该步已经扣除了一次生命值）则从上一个j+1的生命值累加
            if i in L:
                # 循环中的j最大为m，而推导式中有j+1，所以j最大为m-1
                if j < M:
                    # 损失一次生命，加上三种走法
                    dp[i][j] = dp[i - 1][j + 1] + dp[i - 2][j + 1] + dp[i - 3][j + 1]
            else:
                # 没有陷阱，不损失生命，加上三种走法
                dp[i][j] = dp[i - 1][j] + dp[i - 2][j] + dp[i - 3][j]

    # 去掉第一列生命值为0的次数，生命值从1开始到M，求和总次数
    return sum(dp[N + 1][1:])


if __name__ == "__main__":
    assert solve_method(2, 2, 1, [2]) == 4
    assert solve_method(1, 3, 2, [1, 3]) == 1
    assert solve_method(3, 10, 2, [4, 7]) == 504
