#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 211_Alibaba-looks-for-gold-treasure-chests-5.py
@time: 2023/7/22 21:44
@project: huawei-od-python
@desc: 211 阿里巴巴找黄金宝箱（5）
"""


def solve_method(nums, k):
    max_value = 0
    # 使用滑动窗口
    for i in range(len(nums) - k + 1):
        # 计算窗口中的数字和
        max_value = max(sum(nums[i: k + i]), max_value)

    return max_value


if __name__ == '__main__':
    assert solve_method([2, 10, -3, -8, 40, 5], 4) == 39
    assert solve_method([8], 1) == 8
