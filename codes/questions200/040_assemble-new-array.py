#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 040_assemble-new-array.py
@time: 2023/8/22 10:15
@project: huawei-od-python
@desc: 040 组装新的数组
"""


def solve_method(nums, m):
    min_val = nums[0]
    nums = [num for num in nums if num <= m]
    return dfs(nums, m, 0, min_val, 0)


def dfs(nums, m, index, min_val, count):
    if m < 0:
        return count
    if m == 0 or m < min_val:
        return count + 1

    for i in range(index, len(nums)):
        count = dfs(nums, m - nums[i], i, min_val, count)
    return count


if __name__ == "__main__":
    # 2
    # 5
    # N = list(map(int, input().strip().split()))
    # M = int(input().strip())
    # print(solve_method(N, M))

    assert solve_method([2], 5) == 1
    assert solve_method([2, 3], 5) == 2
    assert solve_method([3, 4], 2) == 1
