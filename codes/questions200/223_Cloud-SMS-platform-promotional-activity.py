#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 223_Cloud-SMS-platform-promotional-activity.py
@time: 2023/7/24
@project: huawei-od-python
@desc: 223 Excel 云短信平台优惠活动
"""

max_count = 0


def solve_method(M, P):
    backstracking(P, M, [], 0)
    return max_count


def backstracking(P, n, paths, index):
    global max_count
    # 预算已耗光，计算当前总条数，并记录最大值
    if n == 0:
        count = sum(paths)
        max_count = max(max_count, count)
        return

    for i in range(index, len(P)):
        x = int(P[i])
        paths.append(x)
        # 继续遍历所有可能性
        backstracking(P, n - (i + 1), paths, i + 1)
        paths.pop()


if __name__ == '__main__':
    nums = [10, 20, 30, 40, 60]
    assert solve_method(6, nums) == 70

    nums = [10, 20, 30, 40, 60, 60, 70, 80, 90, 150]
    assert solve_method(15, nums) == 210
