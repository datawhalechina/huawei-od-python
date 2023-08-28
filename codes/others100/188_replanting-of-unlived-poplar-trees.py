#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 188_replanting-of-unlived-poplar-trees.py
@time: 2023/8/27 1:30
@project: huawei-od-python
@desc: 188 补活未成活胡杨树
"""


def solve_method(N, M, trees, K):
    rolls = [0] * N

    for tree in trees:
        rolls[tree - 1] = 1

    left = 0
    right = 0
    count = 0
    result = 0

    while right < N:
        while right < N and count <= K:
            if rolls[right] == 1:
                # 如果找到需要补种的胡杨树，则count累加1
                count += 1
            right += 1

            if count <= K:
                # 如果已经找到K个，计算补种之后的连续胡杨树的个数
                result = max(right - left, result)

        # 找到在[left, right]中第一个为1的位置，然后加1，更新左指针
        left = rolls.index(1, left, right) + 1
        # 减去多加的个数
        count -= 1
    return result


if __name__ == '__main__':
    assert solve_method(10, 3, [2, 4, 7], 1) == 6
    assert solve_method(10, 3, [2, 4, 7], 2) == 8
    assert solve_method(10, 3, [2, 4, 7], 3) == 10
