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

def solve_method(N, T, a):
    # 耗时从小到大排序，以能存活更多人的方案为先
    a.sort()
    dp = [0] * N

    if a[0] > T:
        # 没有人能在敌军到达前过河
        return (0, 0)
    else:
        dp[0] = a[0]
        if N > 1:
            dp[1] = shorter_time(a[0], a[1])
            if dp[1] > T:
                # 两个人无法在敌军到达前完成过河
                return (1, dp[0])
            else:
                # 继续计算更多人需要过河时的耗时
                for i in range(2, N):
                    # 仅剩最后一人未过河的情况，让耗时最少的人划船回来，再计算两人如何划船过河合适
                    a1 = dp[i - 1] + a[0] + shorter_time(a[0], a[i])
                    # 剩两人的情况，需要两趟来回，需要 a0 和 a1 分别划船回来一次
                    a2 = dp[i - 2] + a[0] + shorter_time(a[i - 1], a[i]) + a[1] + shorter_time(a[0], a[1])
                    # 记录更短的那个时间
                    dp[i] = min(a1, a2)
                    if dp[i] > T:
                        return (i, dp[i - 1])
                        break
    return (N, dp[N - 1])
    
if __name__ == '__main__':
    a = [12, 13, 15, 20, 50]
    assert solve_method(5, 43, a) == (3, 40)

    a = [50, 12, 13, 15, 20]
    assert solve_method(5, 130, a) == (5, 128)

    a = [25, 12, 13, 15, 20, 35, 20]
    assert solve_method(7, 171, a) == (7, 171)