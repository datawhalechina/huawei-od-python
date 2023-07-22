#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 217_Alibaba-looks-for-gold-treasure-chests-1.py
@time: 2023/7/23 0:38
@project: huawei-od-python
@desc: 217 阿里巴巴找黄金宝箱（1）
"""


def solve_method(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        # 每次遍历将右侧数字和减去当前数字
        right_sum -= nums[i]
        if left_sum == right_sum:
            # 如果满足相等条件，则返回坐标
            return i
        # 每次遍历将左侧数字和加上当前数字
        left_sum += nums[i]

    # 如果不存在，返回-1
    return -1


if __name__ == '__main__':
    assert solve_method([2, 5, -1, 8, 6]) == 3
    assert solve_method([8, 9]) == -1
    assert solve_method([11]) == 0
