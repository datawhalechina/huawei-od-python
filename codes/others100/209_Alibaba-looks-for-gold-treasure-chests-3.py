#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 209_Alibaba-looks-for-gold-treasure-chests-3.py
@time: 2023/7/22 0:41
@project: huawei-od-python
@desc: 209 阿里巴巴找黄金宝箱（3）
"""


def solve_method(nums, n):
    num_last_index = {}

    for i in range(len(nums)):
        current_num = nums[i]
        if current_num in num_last_index and i - num_last_index[current_num] <= n:
            return num_last_index[current_num]

        num_last_index[current_num] = i

    return -1


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 1], 3) == 0
    assert solve_method([6, 3, 1, 6], 3) == 0
    assert solve_method([5, 6, 7, 5, 6, 7], 2) == -1
