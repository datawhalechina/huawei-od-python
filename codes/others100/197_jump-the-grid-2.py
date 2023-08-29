#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 197_jump-the-grid-2.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 197 跳格子（2）
"""


def dpfunc(nums):
    # dp[i]表示第i个位置的最大和
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        if i == 1:
            # 第二个值为前一个与当前值的最大值
            dp[i] = max(nums[i], dp[i - 1])
        else:
            # 选择前一个值与跳一个之后加上该值的最大值
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[len(nums) - 1]


def solve_method(nums):
    # 去掉最后一个格子或者去掉第一个格子，防止连续
    res = max(dpfunc(nums[:-1]), dpfunc(nums[1:]))
    return res


if __name__ == '__main__':
    assert solve_method([2, 3, 2]) == 3
    assert solve_method([1, 2, 3, 1]) == 4
