#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 181_surviving-on-a-desert-island.py
@time: 2023/9/4 11:11
@project: huawei-od-python
@desc: 004 荒岛求生
"""


def solve_method(nums):
    # 将正数放入右侧列表，负数的绝对值放入左侧列表
    left = [abs(x) for x in nums if x <= 0]
    right = [x for x in nums if x > 0]
    right = right[::-1]

    # 迭代处理左侧和右侧列表
    while right and left:
        if left[0] > right[0]:
            left[0] -= right.pop(0)
        elif left[0] < right[0]:
            right[0] -= left.pop(0)
        else:
            left.pop(0)
            right.pop(0)

    # 输出最终列表的长度之和
    return len(right) + len(left)


if __name__ == "__main__":
    assert solve_method([5, 10, 8, -8, -5]) == 2
