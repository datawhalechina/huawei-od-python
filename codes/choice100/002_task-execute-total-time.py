#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 002_task-execute-total-time.py
@time: 2023/7/11 23:08
@project: huawei-od-python
@desc: 002 任务总执行时长
"""


def solve_method(string):
    str_list = string.split(",")
    taskA = int(str_list[0])
    taskB = int(str_list[1])
    num = int(str_list[2])

    result = []
    for i in range(num + 1):
        total_time = i * taskA + (num - i) * taskB
        result.append(total_time)

    return list(set(result))


if __name__ == '__main__':
    assert solve_method("1,2,3") == [3, 4, 5, 6]
