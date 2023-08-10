#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 087_sound-off-game.py
@time: 2023/8/10 15:43
@project: huawei-od-python
@desc: 087 报数游戏
"""
def solve_method(n, m):
    if m <= 1 or m >= 100:
        return "ERROR!"

    nums = [i for i in range(1, n + 1)]
    # 用于m的计数
    count = 0
    # 当前遍历到的位置
    index = 0
    while len(nums) > 1:
        # 开始计数第count个
        count += 1
        if count == m:
            # 如果到达了第m个，则该位置的人退出
            nums.pop(index)
            # 从0开始重新计数到m
            count = 0
        else:
            # 继续下一个人
            index += 1

        if index == len(nums):
            # 如果已经循环了一圈，则从0位置开始继续循环报数
            index = 0

    return nums[0]


if __name__ == '__main__':
    assert solve_method(15, 3) == 5
    assert solve_method(7, 4) == 2


