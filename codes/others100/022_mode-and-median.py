#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 022_mode-and-median.py
@time: 2023/8/7 13:39
@project: huawei-od-python
@desc: 022 众数和中位数
"""
from collections import Counter


def solve_method(nums):
    # 使用Counter计数
    count = Counter(nums)

    # 获取最大的频次
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]

    # 将数组按照从小到大排序
    sorted_nums = sorted(modes)
    length = len(sorted_nums)

    mid = length // 2
    if length % 2 == 1:
        # 如果数组长度为奇数，中位数为中间的那个元素
        median = sorted_nums[mid]
    else:
        # 如果数组长度为偶数，中位数为中间两个元素的平均值
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) // 2

    return median


if __name__ == '__main__':
    nums = [10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 16]
    assert solve_method(nums) == 21

    nums = [2, 1, 5, 4, 3, 3, 9, 2, 7, 4, 6, 2, 15, 4, 2, 4]
    assert solve_method(nums) == 3

    nums = [5, 1, 5, 3, 5, 2, 5, 5, 7, 6, 7, 3, 7, 11, 7, 55, 7, 9, 98, 9, 17, 9, 15, 9, 9, 1, 39]
    assert solve_method(nums) == 7
