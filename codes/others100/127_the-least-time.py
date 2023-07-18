#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 127_the-least-time.py
@time: 2023/7/18 16:04
@project: huawei-od-python
@desc: 127 最短耗时
"""
from collections import defaultdict


def solve_method(tasks, N):
    # 计算任务频次
    task_count = defaultdict(int)
    for task in tasks:
        task_count[task] += 1
    # 记录最大任务数
    max_count = max(task_count.values())

    max_task_type = [key for key, value in task_count.items() if value == max_count][0]

    # 计算出现次数最多的任务的耗时
    result = (max_count - 1) * (N + 1) + 1
    # 计算冷却时间占用的次数
    free_pos = max_count - 1
    for task_type, count in task_count.items():
        # 插入其他任务
        if task_type != max_task_type:
            # 如果还有空位数，插入进去，减去冷却时间
            for _ in range(count):
                if free_pos > 0:
                    free_pos -= 1
                    result = result - N + 1
                else:
                    # 继续插入其他
                    result += 1

    return max(result, len(tasks))


if __name__ == '__main__':
    assert solve_method([2, 2, 2, 3], 2) == 6
    assert solve_method([2, 2, 2, 3, 3, 1], 2) == 6
    assert solve_method([2, 2, 2, 3, 3, 3], 2) == 6
    assert solve_method([2, 2, 1], 3) == 3
