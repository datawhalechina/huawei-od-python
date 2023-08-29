#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 159-monkey-climbing-the-mountain.py
@time: 2023/8/29 0:21
@project: huawei-od-python
@desc: 159 猴子爬山
"""


def solve_method(n):
    # dp[i]表示到达第i个台阶的跳跃方式数
    dp = [0] * (n + 1)

    # 达到第1个台阶的跳跃方式数为1
    dp[0] = 1

    # 计算每个台阶的跳跃方式数
    for i in range(1, n + 1):
        # 如果当前台阶可以跳1步，则加上从前一个台阶跳上来的方式数
        if i >= 1:
            dp[i] += dp[i - 1]
        # 如果当前台阶可以跳3步，则加上从前三个台阶跳上来的方式数
        if i >= 3:
            dp[i] += dp[i - 3]

    return dp[n]


if __name__ == '__main__':
    assert solve_method(50) == 122106097
    assert solve_method(3) == 2
    assert solve_method(2) == 1
