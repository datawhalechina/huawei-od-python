#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 050_highway-charging-planning.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 050 高速公路充电技术
"""

# 初始化距离和时间列表
pd, pt = [], []
# 初始化备忘录字典，用于存储已计算的解
memo = {}


# 动态规划函数
def dp(pow, dis, N):
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


if __name__ == "__main__":
    # 读取总距离和元素数量
    D, n = map(int, input().split())
    # 初始化距离和时间列表
    pd = [0] * n
    pt = [0] * n
    # 读取每个元素的距离和时间
    for i in range(n):
        pd[i], pt[i] = map(int, input().split())
        pd[i] = D - pd[i]
    # 调用动态规划函数并打印结果
    print(dp(1000, D, n))
