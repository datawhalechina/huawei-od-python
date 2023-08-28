#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 195_peevers-2.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 195 跳房子（2）
"""
import math


def solve_method(target, nums):
    nums = [(n, i) for i, n in enumerate(nums)]
    # 按照值从小到大排序
    nums = sorted(nums, key=lambda x: x[0])
    result = []
    min_index_sum = math.inf
    for i in range(len(nums) - 2):
        # 左指针从当前元素的下一个位置开始
        left = i + 1
        # 右指针从数组的最后一个位置开始
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i][0] + nums[left][0] + nums[right][0]
            index_sum = nums[i][1] + nums[left][1] + nums[right][1]
            if current_sum == target and index_sum < min_index_sum:
                # 如果当前三个步数之和等于房子的总格数，并且索引之和最小，则返回结果
                result = [nums[i], nums[left], nums[right]]
                min_index_sum = index_sum
            elif current_sum < target:
                # 如果小于总格数，则左指针向右移，增大和数
                left += 1
            else:
                # 如果大于总格数，则右指针向左移，减小和数
                right -= 1

    # 按照索引顺序从小到大排序
    result.sort(key=lambda x: x[1])
    return [x[0] for x in result]


if __name__ == '__main__':
    assert solve_method(9, [1, 4, 5, 2, 0, 2]) == [4, 5, 0]
    assert solve_method(9, [1, 5, 2, 0, 2, 4]) == [5, 2, 2]
    assert solve_method(12, [-1, 2, 4, 9]) == [-1, 4, 9]
