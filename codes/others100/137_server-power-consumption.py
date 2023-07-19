#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 137_server-power-consumption.py
@time: 2023/7/19 9:58
@project: huawei-od-python
@desc: 137 服务器耗能
"""
import math


def solve_method(task_times):
    time_powers = [0] * 1000001
    min_time = math.inf
    max_time = -1

    for task_time in task_times:
        start_time = task_time[0]
        end_time = task_time[1]
        min_time = min(min_time, start_time)
        max_time = max(max_time, end_time)
        # 当前时刻的运行任务数
        for i in range(start_time, end_time + 1):
            time_powers[i] += 1

    result = 0
    for i in range(min_time, max_time + 1):
        p = time_powers[i]
        if p == 0:
            # 空载
            result += 1
        elif p == 1:
            # 单任务
            result += 3
        else:
            # 多任务
            result += 4

    return result


if __name__ == '__main__':
    task_times = [[2, 5], [8, 9]]
    assert solve_method(task_times) == 20

    task_times = [[4, 8], [1, 6], [2, 9]]
    assert solve_method(task_times) == 34
