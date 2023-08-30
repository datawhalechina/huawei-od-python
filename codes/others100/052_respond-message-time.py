#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 052_respond-message-time.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 052 报文响应时间
"""
import math


def solve_method(N, response_times):
    min_value = math.inf
    for [T, M] in response_times:
        if M >= 128:
            # 提取M的位4-7，与0x10进行逻辑或操作，然后根据M的位0-2值左移
            M = ((M >> 3) & 0xF | 0x10) << (M & 0x7 + 3)
        resp_time = T + M
        if resp_time < min_value:
            min_value = resp_time

    return min_value


if __name__ == '__main__':
    response_times = [[0, 20],
                      [1, 10],
                      [8, 20]]
    assert solve_method(3, response_times) == 11

    response_times = [[0, 255],
                      [200, 60]]
    assert solve_method(2, response_times) == 260
