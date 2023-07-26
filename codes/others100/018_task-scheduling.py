#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 018_task-scheduling.py
@time: 2023/7/26 23:12
@project: huawei-od-python
@desc: 018 任务调度
"""


def solve_method(tasks):
    time = 0
    waiting_list = []
    result = []

    while len(tasks) > 0:
        current_task = next((task for task in tasks if task[3] == time), None)

        if current_task is not None:
            waiting_list.append(current_task)
            # 按优先级从高到低排序
            waiting_list = sorted(waiting_list, key=lambda x: -x[1])
            # 取出优先级最高的任务执行
            current_task = waiting_list[0]
        else:
            # 空闲时间，从等待列表中取出优先级最高的任务执行
            if len(waiting_list) != 0:
                current_task = waiting_list[0]

        if current_task is not None:
            current_task[2] -= 1
            if current_task[2] == 0:
                # 任务执行完毕
                result.append([current_task[0], time + 1])
                tasks.remove(current_task)
                waiting_list.remove(current_task)

        time += 1

    return result


if __name__ == '__main__':
    tasks = [[1, 3, 5, 1],
             [2, 1, 5, 10],
             [3, 2, 7, 12],
             [4, 3, 2, 20],
             [5, 4, 9, 21],
             [6, 4, 2, 22]]
    assert solve_method(tasks) == [[1, 6], [3, 19], [5, 30], [6, 32], [4, 33], [2, 35]]
