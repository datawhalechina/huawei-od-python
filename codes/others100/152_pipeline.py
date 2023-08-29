#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 152_pipeline.py
@time: 2023/8/29 0:18
@project: huawei-od-python
@desc: 152 流水线
"""


def solve_method(m, n, job_times):
    # 将作业处理时间按升序排序
    job_times.sort()
    # 初始化流水线的处理时间为0
    pipelines = [0] * m

    for i in range(n):
        # 找到处理时间最短的流水线
        min_pipeline = min(pipelines)
        index = pipelines.index(min_pipeline)
        # 将当前作业分配给最短处理时间的流水线
        pipelines[index] += job_times[i]

    total_time = max(pipelines)

    return total_time


if __name__ == '__main__':
    assert solve_method(3, 5, [8, 4, 3, 2, 10]) == 13
