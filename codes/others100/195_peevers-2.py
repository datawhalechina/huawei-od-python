#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 195_peevers-2.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 195 跳房子（2）
"""


def dfs(nums, remaining, combination, indices, index):
    global minIndexSum, targetCount, result

    if remaining == 0:
        total = 0
        indexSumTemp = 0
        for i in range(3):
            total += combination[i]
            indexSumTemp += indices[i]
        if total == targetCount and indexSumTemp < minIndexSum:
            minIndexSum = indexSumTemp
            result = combination[:]
    else:
        for i in range(index, len(nums)):
            combination.append(nums[i])
            indices.append(i)
            dfs(nums, remaining - 1, combination, indices, i + 1)
            combination.pop()
            indices.pop()


minIndexSum = float('inf')
targetCount = int(input())
nums = list(map(int, input().strip(' [\] ').split(',')))
result = []
dfs(nums, 3, [], [], 0)
output = '[' + ', '.join(map(str, result)) + '] '
print(output)
