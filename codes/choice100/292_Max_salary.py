#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jack Lee C.S.
@file: 292_Max_salary
@time: 2023/07/12 14:39
@project: huawei-od-python
@desc: 292_Max_salary
@tags: Dynamic-Programming
"""
def solution(t, n, jobs):
	m_t = min(jobs, key = lambda x: x[0])[0] # min hours of jobs
	dp = [[0] * (t + 1) for _ in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(m_t, t + 1):
			job = jobs[i - 1]
			v = dp[i - 1][j]
			new_v = job[1] + dp[i - 1][j - job[0]] if job[0] <= j else 0
			dp[i][j] = max(v, new_v)
    # return dp[n][t]
