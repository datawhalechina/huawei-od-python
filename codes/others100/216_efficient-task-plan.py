#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 216_efficient-task-plan.py
@time: 2023/7/22 23:52
@project: huawei-od-python
@desc: 216 高效的任务规划
"""


def solve_method(tasks):
    result = []
    for task in tasks:
        N = len(task)
        # 按照运行时间从大到小排列
        jobs = sorted(task, key=lambda x: x[1], reverse=True)

        # 总任务时间
        time = 0
        # 还需要等待的执行时间
        remaining = 0
        for job in jobs:
            # 累加配置时间
            time += job[0]
            if remaining <= 0:
                # 如果还需等待的执行时间小于当前机器的配置时间，则等于当前机器的执行时间
                remaining = job[1]
            else:
                # 如果执行时间还有，则减去当前机器的配置时间，并加上当前机器的执行时间
                remaining -= job[0]
                remaining += job[1]

        # 最后再加上等待的执行时间
        time += remaining
        result.append(time)

    return result


if __name__ == '__main__':
    tasks = [[(2, 2)]]
    assert solve_method(tasks) == [4]

    tasks = [[(1, 1), (2, 2)],
             [(1, 1), (2, 2), (3, 3)]]
    assert solve_method(tasks) == [5, 9]
