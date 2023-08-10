#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 086_sound-off.py
@time: 2023/8/10 15:30
@project: huawei-od-python
@desc: 086 报数
"""


def solve_method(M):
    if M <= 1 or M >= 100:
        return "ERROR!"

    nums = [i for i in range(1, 101)]
    # 用于M的计数
    count = 0
    # 当前遍历到的位置
    index = 0
    while len(nums) >= M:
        # 开始计数第count个
        count += 1
        if count == M:
            # 如果到达了第M个，则该位置的人退出
            nums.pop(index)
            # 从0开始重新计数到M
            count = 0
        else:
            # 继续下一个人
            index += 1

        if index == len(nums):
            # 如果已经循环了一圈，则从0位置开始继续循环报数
            index = 0

    return nums


if __name__ == '__main__':
    assert solve_method(3) == [58, 91]
    assert solve_method(4) == [34, 45, 97]
