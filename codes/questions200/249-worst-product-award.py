#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 249-worst-product-award.py
@time: 2023/8/21 15:19
@project: huawei-od-python
@desc: 249 最差产品奖
"""


def solve_method(M, scores):
    min_scores = []
    for i in range(len(scores) - M + 1):
        min_score = min(scores[i:i + M])
        min_scores.append(min_score)
    return min_scores


if __name__ == "__main__":
    # 3
    # 12,3,8,6,5
    # M = int(input())
    # scores = list(map(int, input().split(',')))
    # print(solve_method(M, scores))

    assert solve_method(3, [12, 3, 8, 6, 5]) == [3, 3, 5]
