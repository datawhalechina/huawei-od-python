#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 189_watch-the-performance.py
@time: 2023/8/27 1:30
@project: huawei-od-python
@desc: 189 观看文艺汇演问题、最多能看几场演出
"""


def solve_method(show_times):
    times = []
    for start_time, duration in show_times:
        times.append([start_time, start_time + duration])

    # 按照结束时间进行排序
    times.sort(key=lambda x: x[1])
    result = 1

    prev_start_time = times[0][1]
    for i in range(1, len(times)):
        start_time, end_time = times[i]
        if start_time - prev_start_time >= 15:
            # 如果15分钟能赶得上，则可以看这场演出
            result += 1
            prev_start_time = end_time

    return result


if __name__ == '__main__':
    show_times = [[720, 120],
                  [840, 120]]
    assert solve_method(show_times) == 1

    show_times = [[0, 60],
                  [90, 60]]
    assert solve_method(show_times) == 2
