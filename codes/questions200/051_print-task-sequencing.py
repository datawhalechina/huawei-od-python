#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 051_print-task-sequencing.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 051 打印任务排序
"""


def solve_method(tasks):
    task_index = [(task, idx) for idx, task in enumerate(tasks)]
    n = len(tasks)

    # 标记当前优先级最高的任务
    tasks.sort()
    max_idx = n - 1
    # 标记打印顺序
    res = [0] * n
    printIdx = 0
    while task_index:
        task, idx = task_index.pop(0)
        # 是优先级最高的任务
        if task == tasks[max_idx]:
            res[idx] = printIdx
            max_idx -= 1
            printIdx += 1
        # 不是优先级最高的任务，加入队尾
        else:
            task_index.append((task, idx))
    return res


if __name__ == '__main__':
    assert solve_method([9, 3, 5]) == [0, 2, 1]
    assert solve_method([1, 2, 2]) == [2, 0, 1]
