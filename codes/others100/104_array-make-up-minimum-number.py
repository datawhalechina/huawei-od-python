#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 104_array-make-up-minimum-number.py
@time: 2023/7/25 21:40
@project: huawei-od-python
@desc: 104 数组组成的最小数字
"""


def solve_method(arr):
    len_arr = len(arr)
    arr.sort()
    nums_len = 2 if len_arr == 2 else 3
    nums_str = [str(arr[i]) for i in range(nums_len)]
    nums_str.sort()
    result = int(''.join(nums_str))
    return result


if __name__ == "__main__":
    assert solve_method([21, 30, 62, 5, 31]) == 21305
    assert solve_method([5,21]) == 215
