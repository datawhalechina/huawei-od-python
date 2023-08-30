#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 056_the-length-of-substring.py
@time: 2023/08/11 0:47
@project: huawei-od-python
@desc: 056 子序列长度
"""


def solve_method(nums, target_sum):
    max_len = -1

    if sum(nums) < target_sum:
        return -1

    left, right = 0, 1
    while left < len(nums):
        sub_sum = sum(nums[left:right])
        if right == len(nums) - 1 and sub_sum < target_sum:
            break

        if sub_sum == target_sum:
            length = right - left
            if max_len < length:
                max_len = length
            left += 1
        elif sub_sum > target_sum:
            left += 1
        else:
            right += 1

    return max_len


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 2]
    assert solve_method(nums, 6) == 3

    nums = [1, 2, 3, 4, 2]
    assert solve_method(nums, 20) == -1
