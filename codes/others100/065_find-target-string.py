#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 065_find-target-string
@time:  21/8/2023 下午 4:32
@project:  huawei-od-python 
"""


def solve_method(nums, target):
    def infect(row, col, k, m, n, nums, target):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or (k < len(target) and nums[row][col] != target[k]):
            return []
        if k == len(target) - 1 and nums[row][col] == target[k]:
            return [[row, col]]

        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            value = nums[row][col]
            nums[row][col] = '#'
            res = infect(row + d1, col + d2, k + 1, m, n, nums, target)
            nums[row][col] = value
            if res:
                return [[row, col]] + res
        return []

    m, n = len(nums), len(nums[0])
    for i in range(m):
        for j in range(n):
            if nums[i][j] == target[0]:
                ans = infect(i, j, 0, m, n, nums, target)
                if ans:
                    return ','.join([','.join([str(item[0]), str(item[1])]) for item in ans])
    return 'N'


if __name__ == '__main__':
    n = int(input().strip())
    nums = []
    for _ in range(n):
        nums.append(input().strip().split(','))
    target = input().strip()
    res = solve_method(nums, target)
    print(res)
