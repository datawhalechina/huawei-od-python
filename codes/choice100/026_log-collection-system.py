#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 026_log-collection-system.py
@time: 2023/7/14 23:04
@project: huawei-od-python
@desc: 026 日志采集系统
"""


def calc_score(arr, cur_val):
    score = 0
    # 累计日志条数
    total = 0
    for i in range(cur_val + 1):
        if total + arr[i] < 100:
            # 直接奖励分
            score += arr[i]
            # 延迟上报扣分
            score -= arr[i] * (cur_val - i)
            total += arr[i]
        else:
            # 超过100条，强制上报
            score = 100 - total
            return score

    return score


def solve_method(arr):
    score = 0

    if len(arr) > 0 and arr[0] >= 100:
        return 100

    for i in range(len(arr)):
        score = max(score, calc_score(arr, i))

    return score


if __name__ == '__main__':
    assert solve_method([1, 98, 1]) == 98
    assert solve_method([50, 60, 1]) == 50
