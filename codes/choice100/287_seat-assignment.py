#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 287_seat-assignment.py
@time: 2023/7/14 20:03
@project: huawei-od-python
@desc: 287 新员工座位安排系统
"""


def solve_method(arr):
    max_value = 0
    max_pos = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if i == 0:
                # 最左侧
                friend_value = arr[i + 1]
            elif i == len(arr) - 1:
                # 最右侧
                friend_value = arr[i - 1]
            else:
                # 其他区域
                friend_value = arr[i - 1] + arr[i + 1]
            # 比较友好度
            if friend_value > max_value:
                max_value = friend_value
                max_pos = i
    return max_pos + 1


if __name__ == '__main__':
    assert solve_method([0, 1, 0]) == 1
    assert solve_method([1, 1, 0, 1, 2, 1, 0]) == 3
