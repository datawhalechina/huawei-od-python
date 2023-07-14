#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 280_integration-testing-of-microservices.py
@time: 2023/7/14 11:41
@project: huawei-od-python
@desc: 280 微服务的集成测试
"""


def dfs(arr, k):
    max_time = 0
    # 遍历服务
    for i in range(len(arr)):
        # 得到服务k启动依赖的服务
        if arr[k][i] != 0 and i != k:
            # 计算启动依赖服务的最大耗时，并记录到总耗时中
            max_time = max(max_time, dfs(arr, i))
    return max_time + arr[k][k]


def solve_method(arr, k):
    total_time = dfs(arr, k - 1)
    return total_time


if __name__ == '__main__':
    k = 3
    useTime = [
        [5, 0, 0],
        [1, 5, 0],
        [0, 1, 5]
    ]
    assert solve_method(useTime, k) == 15

    k = 2
    useTime = [
        [5, 0, 0],
        [1, 10, 1],
        [1, 0, 11]
    ]
    assert solve_method(useTime, k) == 26

    k = 4
    useTime = [
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [1, 1, 4, 0],
        [1, 1, 1, 5],
    ]
    assert solve_method(useTime, k) == 12

    k = 5
    useTime = [
        [1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [1, 1, 3, 0, 0],
        [1, 1, 0, 4, 0],
        [0, 0, 1, 1, 5]
    ]
    assert solve_method(useTime, k) == 11
