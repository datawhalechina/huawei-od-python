#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 050_highway-charging-planning.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 050 高速公路充电技术
"""


# 动态规划函数
def dp(pow, dis, N):
    global pd, pt, memo
    # 如果当前功率大于或等于距离，则返回所需的时间
    if pow >= dis:
        return dis // 100
    key = f"{pow},{dis}"
    if key in memo:
        return memo[key]
    res = float('inf')
    # 遍历所有可能的选择
    for i in range(N):
        # 跳过不合适的选择
        if dis - pow > pd[i] or pd[i] == dis or dp(1000, pd[i], N) == -1:
            continue
        # 计算当前选择的结果，并与之前的结果进行比较
        res = min(res, (dis - pd[i] // 100 + pt[i] + 1 + dp(1000, pd[i], N)))

    # 如果没有找到解，则返回-1
    memo[key] = -1 if res == float('inf') else res
    return memo[key]


def solve_method(D, N, sites):
    global pd, pt, memo
    # 初始化备忘录字典，用于存储已计算的解
    memo = {}
    # 初始化距离和时间列表
    pd = [0] * N
    pt = [0] * N
    # 读取每个元素的距离和时间
    for i in range(N):
        pd[i], pt[i] = sites[i]
        pd[i] = D - pd[i]
    # 调用动态规划函数并打印结果
    result = dp(1000, D, N)
    return result


if __name__ == "__main__":
    sites = [[300, 2],
             [600, 1],
             [1000, 0],
             [1200, 0]]
    assert solve_method(1500, 4, sites) == 16

    sites = [[300, 0],
             [600, 0]]
    assert solve_method(800, 2, sites) == 8
