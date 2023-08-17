#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 064_find-max-value
@time:  17/8/2023 上午 11:44
@project:  huawei-od-python 
"""

def solve_method(nums):
    m, n = len(nums), len(nums[0])
    if m < 1:
        return 0

    def infect(row, col, nums, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or nums[row][col] == 0 or nums[row][col] == -1:
            return 0
        else:
            value = nums[row][col]
            nums[row][col] = -1
            for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                value += infect(row + d1, col + d2, nums, m, n)
            return value

    ans = -1
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1 or nums[i][j] == 2:
                value = infect(i, j, nums, m, n)
                if value > ans:
                    ans = value
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    nums = [list(map(int, list(input().strip()))) for _ in range(n)]
    res = solve_method(nums)
    print(res)
