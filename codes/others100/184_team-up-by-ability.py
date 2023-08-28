#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 184_team-up-by-ability.py
@time: 2023/8/27 1:28
@project: huawei-od-python
@desc: 184 能力组队
"""


def solve_method(nums, min_power):
    # 过滤出小于最低能力值的人
    arr = sorted(filter(lambda x: x < min_power, nums))
    # 大于等于最低能力值的人，都可以自成一队
    count = len(nums) - len(arr)
    # 双指针遍历
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] >= min_power:
            # 如果最小值和最大值加起来小于最低能力值，可以组成一队
            count += 1
            i += 1
            j -= 1
        else:
            # 否则左指针向右移
            i += 1
    return count


if __name__ == '__main__':
    assert solve_method([3, 1, 5, 7, 9], 8) == 3
    assert solve_method([3, 1, 5, 7, 9, 2, 6], 8) == 4
    assert solve_method([3, 1, 5, 6, 9], 8) == 2
