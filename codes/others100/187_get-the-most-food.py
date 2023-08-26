#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 187_get-the-most-food.py
@time: 2023/8/27 1:30
@project: huawei-od-python
@desc: 187 获取最多食物
"""

n = int(input())
nodes = {}
for i in range(n):
    id, pid, val = map(int, input().split(" "))
    if id < 0 or id >= n or pid < -1 or pid >=n:
        continue
    nodes[id] = [pid, val]
dp = {}

def dfs(i):
    if i not in dp:
        if nodes[i][0] == -1:
            dp[i] = nodes[i][1]
        else:
            dp[i] = max(nodes[i][1], nodes[i][1] + dfs(nodes[i][0]))
    return dp[i]

max_val = -float("inf")
for i in reversed(range(n)):
    if i not in nodes:
        continue
    max_val = max(max_val, dfs(i))

print(max_val)