#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 071_seat-adjustment
@time:  24/8/2023 上午 10:31
@project:  huawei-od-python 
"""


def solve_method(nums):
    if len(nums) < 3:
        if sum(nums) > 0:
            return 0
        else:
            return 1
    if sum(nums) >= len(nums) // 2 + 1:
        return 0
    ans = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            continue
        elif i == 0 and nums[i + 1] == 0:
            ans += 1
            nums[i] = 1
        elif i == n - 1 and nums[i - 1] == 0:
            ans += 1
        else:
            if nums[i - 1] == 0 and nums[i + 1] == 0:
                ans += 1
                nums[i] = 1
    return ans


if __name__=='__main__':
    nums = list(map(int,input().strip().split(' ')))
    res = solve_method(nums)
    print(res)




