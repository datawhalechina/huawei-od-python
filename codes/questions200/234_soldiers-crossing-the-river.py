#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 234_soldiers-crossing-the-river.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 234 士兵过河 
"""


def shorter_time(a, b):
    # 返回是一人划船 或 两人一起划船 耗时少的时间
    return a * 10 if a * 10 < b else b


def solve_method(N, T, arr):
    # 将过河时长从小到大排序
    arr.sort()
    # dp[i]表示存活i人的最短过河时间
    dp = [0] * N

    if arr[0] > T:
        # 没有人能在敌军到达前过河
        return 0, 0
    else:
        dp[0] = arr[0]
        if N > 1:
            dp[1] = shorter_time(arr[0], arr[1])
            if dp[1] > T:
                # 两个人无法在敌军到达前完成过河
                return 1, dp[0]
            else:
                # 继续计算更多人需要过河的时长
                for i in range(2, N):
                    # 仅剩最后一人未过河的情况，让耗时最少的人划船返回，再计算两人划船过河的时长
                    a1 = dp[i - 1] + arr[0] + shorter_time(arr[0], arr[i])
                    # 剩两人的情况，需要来回两趟，需要a[0]和a[1]分别划船回来一次，再最后一起划船过河
                    a2 = dp[i - 2] + arr[0] + shorter_time(arr[i - 1], arr[i]) + arr[1] + shorter_time(arr[0], arr[1])
                    # 记录以上两个时长中更短的那个时长
                    dp[i] = min(a1, a2)
                    if dp[i] > T:
                        return i, dp[i - 1]
    return N, dp[N - 1]


if __name__ == '__main__':
    arr = [12, 13, 15, 20, 50]
    assert solve_method(5, 43, arr) == (3, 40)

    arr = [50, 12, 13, 15, 20]
    assert solve_method(5, 130, arr) == (5, 128)

    arr = [25, 12, 13, 15, 20, 35, 20]
    assert solve_method(7, 171, arr) == (7, 171)
