#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 002_GPU-scheduling.py
@time: 2023/7/26 9:46
@project: huawei-od-python
@desc: 002 GPU调度
"""


def solve_method(n, jobs):
    # 初始化总运行时间和等待时间
    total_time, remaining_time = 0, 0
    for job in jobs:
        if job + remaining_time > n:
            # 计算等待时间
            remaining_time = job + remaining_time - n
        else:
            # 无需等待
            remaining_time = 0
        total_time += 1

    # 继续等待作业完成，每载入n个作业，总时间累加1
    while remaining_time > 0:
        remaining_time -= n
        total_time += 1

    return total_time


if __name__ == '__main__':
    assert solve_method(3, [1, 2, 3, 4, 5]) == 6
    assert solve_method(4, [5, 4, 1, 1, 1]) == 5
