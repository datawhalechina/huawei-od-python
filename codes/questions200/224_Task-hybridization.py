#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 224_Task-hybridization.py
@time: 2023/7/25
@project: huawei-od-python
@desc: 224 任务混部
"""
from collections import defaultdict


def solve_method(tasks):
    # 时刻所占服务器数量的字典，key为时刻，value为服务器数量
    time_servers = defaultdict(int)

    for task in tasks:
        parallelism = task[2]
        for i in range(task[0], task[1]):
            time_servers[i] += parallelism

    # 取出服务器数量最大的那个
    return max(time_servers.values())


if __name__ == '__main__':
    tasks = [[2, 3, 1],
             [6, 9, 2],
             [0, 5, 1]]

    assert solve_method(tasks) == 2

    tasks = [[3, 9, 2],
             [4, 7, 3]]

    assert solve_method(tasks) == 5
