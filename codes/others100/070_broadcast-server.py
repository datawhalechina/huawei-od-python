#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 070_broadcast-server
@time:  23/8/2023 下午 7:46
@project:  huawei-od-python 
"""


def solve_method(nums):
    def dfs(nums, visited, index):
        visited[index] = True
        for j in range(len(nums)):
            if nums[index][j] == 1 and not visited[j]:
                dfs(nums, visited, j)

    n = len(nums)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(nums, visited, i)
            count += 1
    return count


if __name__ == '__main__':
    nums = [list(map(int, input().strip().split(' ')))]
    n = len(nums[0])
    for _ in range(n-1):
        nums.append(list(map(int, input().strip().split(' '))))
    res = solve_method(nums)
    print(res)
