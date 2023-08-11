#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 018_task-scheduling.py
@time: 2023/7/26 23:12
@project: huawei-od-python
@desc: 018 任务调度
"""

import heapq


def solve_method(tasks):
    """
    :param tasks: 任务列表：每个元素有4个值，分别是任务ID、任务优先级、执行时间和到达时间
    :return:
    """
    time = 0
    waiting_list = []
    result = []
    # 对tasks重新生成，便于进入堆，每个元素的4个值分别是任务优先级、到达时间、执行时间和任务ID
    for i, task in enumerate(tasks):
        task_id, priority, duration, arrival_time = task
        tasks[i] = [-priority, arrival_time, duration, task_id]

    while len(tasks) > 0:
        current_task = next((task for task in tasks if task[1] == time), None)

        if current_task is not None:
            # 堆顶为优先级最高的任务
            heapq.heappush(waiting_list, current_task)
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
                result.append([current_task[3], time + 1])
                tasks.remove(current_task)
                # 从waiting_list堆中移除掉堆顶优先级最大的元素
                heapq.heappop(waiting_list)

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
