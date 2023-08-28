#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 198_kick-stones.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 198 踢石子问题
"""


def solve_method(K):
    if K <= 1 or K >= 100:
        return "ERROR!"

    nums = [i for i in range(1, 101)]
    # 用于K的计数
    count = 0
    # 当前遍历到的位置
    index = 0
    while len(nums) >= K:
        # 开始计数第count个
        count += 1
        if count == K:
            # 如果到达了第K个，将此石子踢出
            nums.pop(index)
            # 从0开始重新计数到K
            count = 0
        else:
            # 继续下一个石子
            index += 1

        if index == len(nums):
            # 如果已经循环了一圈，则从0位置开始继续循环报数
            index = 0

    return nums


if __name__ == '__main__':
    assert solve_method(3) == [58, 91]
