#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 101_the-most-economical-way-to-back-up-data.py
@time: 2023/7/25 11:20
@project: huawei-od-python
@desc: 101 数据最节约的备份方法
"""


def dfs(arr, num):
    if len(arr) <= 1:
        num += len(arr)
        return num

    if arr[0] + arr[-1] < 500:
        arr[-1] += arr[0]
        arr.pop(0)
    elif arr[0] + arr[-1] == 500:
        arr.pop()
        arr.pop(0)
        num += 1
    else:
        arr.pop()
        num += 1
    return dfs(arr, num)


def solve_method(arr):
    arr.sort()
    result = dfs(arr, 0)
    return result


if __name__ == '__main__':
    assert solve_method([100, 500, 300, 200, 400]) == 3
    assert solve_method([100, 100, 200, 300]) == 2
