#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 067_search-continuous-scope
@time:  13/8/2023 下午 11:38
@project:  huawei-od-python 
"""


def solve_method(nums, target):
    n = len(nums)
    ans = 0
    if sum(nums) < target:
        return ans
    for i in range(n):
        for j in range(i + 1, n + 1):
            if sum(nums[i:j]) >= target:
                ans += n - j + 1
                break
    return ans

if __name__ == '__main__':
    N, x = list(map(int, input().strip().split(' ')))
    nums = list(map(int, input().strip().split(' ')))
    res = solve_method(nums, x)
    print(res)