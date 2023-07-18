#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 125_minimum-number-of-exchanges.py
@time: 2023/7/18 15:09
@project: huawei-od-python
@desc: 125 最少交换次数
"""


def solve_method(arr, k):
    # 得到小于k的掩码数组
    less_k_arr = [1 if n < k else 0 for n in arr]
    n = len(less_k_arr)
    # 得到需要相邻的数字个数
    m = sum(less_k_arr)

    # 使用滑动窗口求和，得到窗口内已满足条件的个数
    dp = [sum(less_k_arr[i: i + m]) for i in range(n)]
    # 得到最少交换次数
    result = m - max(dp)
    return result


if __name__ == '__main__':
    assert solve_method([1, 3, 1, 4, 0], 2) == 1
    assert solve_method([0, 0, 0, 1, 0], 2) == 0
    assert solve_method([2, 3, 2], 1) == 0
