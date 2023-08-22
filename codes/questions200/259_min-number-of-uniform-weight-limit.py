#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 259_min-number-of-uniform-weight-limit.py
@time: 2023/8/22 10:15
@project: huawei-od-python
@desc: 259 统一限载货物数最小值
"""


def solve_method(length, goods, types, k):
    drys, wets = [], []
    for i in range(length):
        if types[i] == 0:
            drys.append(goods[i])
        else:
            wets.append(goods[i])
    min_weight_drys = get_min_weight(drys, k)
    min_weight_wets = get_min_weight(wets, k)
    return max(min_weight_drys, min_weight_wets)


def get_min_weight(goods, k):
    min_weight = max(goods)
    max_weight = sum(goods)
    while min_weight < max_weight:
        mid = (min_weight + max_weight) // 2
        if check(goods, mid, [0] * k, 0):
            max_weight = mid
        else:
            min_weight = mid + 1
    return min_weight


def check(goods, weight, vans, index):
    # 判断所有货物是否都装完了
    if index == len(goods):
        return True
    for i in range(len(vans)):
        if vans[i] + goods[index] <= weight:
            vans[i] += goods[index]
            if check(goods, weight, vans, index + 1):
                return True
            vans[i] -= goods[index]
    return False


if __name__ == "__main__":
    # 4
    # 3 2 6 3
    # 0 1 1 0
    # 2
    # length = int(input().strip())
    # goods = list(map(int, input().strip().split()))
    # types = list(map(int, input().strip().split()))
    # k = int(input().strip())
    # print(solve_method(length, goods, types, k))

    assert solve_method(4, [3, 2, 6, 3], [0, 1, 1, 0], 2) == 6
    assert solve_method(4, [3, 2, 6, 8], [0, 1, 1, 1], 1) == 16
