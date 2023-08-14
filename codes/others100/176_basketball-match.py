#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 176_basketball-match.py
@time: 2023/8/8 23:28
@project: huawei-od-python
@desc: 176 篮球比赛
"""


def solve_method(s):
    s = list(map(int, s.split()))
    # 转换为背包问题，尽量装满一半，那么两队差距最小
    bags = sum(s)//2
    
    # 装满i时的最大重量
    dp = [0]*(bags+1)
    for i in s:
        for j in reversed(range(i, bags+1)):
            dp[j] = max(dp[j], dp[j-i]+i)
    return sum(s) - 2*dp[-1]


if __name__ == '__main__':
    assert solve_method("1 2 3 4 5 6 7 8 9 10") == 1
