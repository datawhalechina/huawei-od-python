#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 001_AI-Processor-Combination.py
@time: 2023/7/11 15:58
@project: huawei-od-python
@desc: 001 AI处理器组合
"""
from itertools import combinations


def solve_method(arr, num):
    result = []

    first = [n for n in arr if n < 4]
    second = [n for n in arr if n >= 4]
    first_nums = len(first)
    second_nums = len(second)

    if num == 1:
        result.extend(cpu1(first, first_nums, second, second_nums))
    elif num == 2:
        result.extend(cpu2(first, first_nums, second, second_nums))
    elif num == 4:
        if first_nums == 4:
            result.append([n for n in range(4)])
        if second_nums == 4:
            result.append([n for n in range(4, 8)])
    elif num == 8:
        if first_nums == 4 and second_nums == 4:
            result.append([n for n in range(8)])

    return result


def cpuN(first, first_nums, second, second_nums, priority, k) -> list:
    cpus = []

    is_fit = False
    for p in priority:
        if p == first_nums:
            cpus.extend([list(n) for n in combinations(first, k)])
            is_fit = True
        if p == second_nums:
            cpus.extend([list(n) for n in combinations(second, k)])
            is_fit = True
        if is_fit:
            break

    return cpus


def cpu1(first, first_nums, second, second_nums) -> list:
    return cpuN(first, first_nums, second, second_nums, [1, 3, 2, 4], 1)


def cpu2(first, first_nums, second, second_nums) -> list:
    return cpuN(first, first_nums, second, second_nums, [2, 4, 3], 2)


if __name__ == '__main__':
    assert solve_method([0, 1, 4, 5, 6, 7], 4) == [[4, 5, 6, 7]]
    assert solve_method([0, 1, 4, 5, 6, 7], 1) == [[0], [1]]
    print(solve_method([0, 1, 2, 4, 5, 6], 2))
