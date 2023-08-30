#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 054_shout-seven.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 054 喊七
"""


def solve_method(nums):
    result = [0] * len(nums)
    N = 7 * (sum(nums) + len(nums))
    j = 0
    for i in range(1, N):
        # 判断当前j在列表中的位置
        j %= len(nums)
        # 如果当前数字是7的倍数或者含有7
        if i % 7 == 0 or '7' in str(i):
            result[j] += 1
            # 如果结果列表的总和等于输入数字的总和，终止循环
            if sum(result) == sum(nums):
                break
        j += 1

    return result


if __name__ == "__main__":
    assert solve_method([0, 1, 0]) == [1, 0, 0]
    assert solve_method([0, 0, 0, 2, 1]) == [0, 2, 0, 1, 0]
