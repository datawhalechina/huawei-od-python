#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 020_find-number.py
@time: 2023/7/14 16:12
@project: huawei-od-python
@desc: 020 找数字
"""
import math
from collections import defaultdict


def solve_method(arr):
    n = len(arr)
    m = len(arr[0])
    num_pos = defaultdict(list)
    # 统计每个数字的所在位置
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            num_pos[num].append((i, j))

    # 初始化列表，最小位置都设置为-1
    result = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            num = arr[i][j]
            all_pos = num_pos[num]

            min_diff = math.inf
            if len(all_pos) != 1:
                for pos in all_pos:
                    if i == pos[0] and j == pos[1]:
                        continue
                    # 计算距离值
                    diff = abs(i - pos[0]) + abs(j - pos[1])
                    # 得到最近距离
                    min_diff = min(min_diff, diff)
                result[i][j] = min_diff

    return result


if __name__ == '__main__':
    arr = [
        [0, 3, 5, 4, 2],
        [2, 5, 7, 8, 3],
        [2, 5, 4, 2, 4]
    ]
    assert solve_method(arr) == [[-1, 4, 2, 3, 3], [1, 1, -1, -1, 4], [1, 1, 2, 3, 2]]
