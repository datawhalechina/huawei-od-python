#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jack Lee C.S.
@file: 029_max-salary.py
@time: 2023/07/12 14:39
@project: huawei-od-python
@desc: 029 最大报酬
"""


def solve_method(T, jobs):
    N = len(jobs)
    # 最短工作时长
    min_time = min(jobs, key=lambda x: x[0])[0]
    # dp[i][j]表示在前i个任务中，花费时间不超过j的最大报酬
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(min_time, T + 1):
            job = jobs[i - 1]
            w1 = dp[i - 1][j]
            w2 = job[1] + dp[i - 1][j - job[0]] if job[0] <= j else 0
            dp[i][j] = max(w1, w2)
    return dp[N][T]


if __name__ == '__main__':
    jobs = [[20, 10],
            [20, 20],
            [20, 5]]
    assert solve_method(40, jobs) == 30
