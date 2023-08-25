#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 070_broadcast-server
@time:  2023/8/23 19:46
@project:  huawei-od-python
@desc: 070 广播服务器
"""


def solve_method(nums):
    N = len(nums)
    cover = set()
    count = 0

    for i in range(N):
        if i not in cover:
            count += 1
            cover.add(i)
        for j in filter(lambda x: x != i, range(N)):
            if nums[i][j] == 1:
                cover.add(j)

    return count


if __name__ == '__main__':
    nums = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
    assert solve_method(nums) == 3

    nums = [[1, 1],
            [1, 1]]
    assert solve_method(nums) == 1
