#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 197_jump-the-grid-2.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 197 跳格子
"""


def dpfunc(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        if i == 1:
            dp[i] = max(nums[i], dp[i - 1])
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[len(nums) - 1]


def main():
    strings = input().split()
    if len(strings) == 1:
        print(int(strings[0]))
        return

    numsStart = [int(x) for x in strings[:-1]]
    numsEnd = [int(x) for x in strings[1:]]

    res = max(dpfunc(numsStart), dpfunc(numsEnd))
    print(res)


main()
