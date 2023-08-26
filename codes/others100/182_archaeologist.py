#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 182_archaeologist.py
@time: 2023/8/27 1:26
@project: huawei-od-python
@desc: 182 考古学家
"""

import itertools


def solve_method(n, segment):
    segement = segment.split(" ")
    permutation_list = list(itertools.permutations(segement))
    permutation_list = list(set(["".join(i) for i in permutation_list]))
    permutation_list.sort()
    for item in permutation_list:
        print(item)


def main():
    n = int(input().strip())
    segment = input().strip()
    solve_method(n, segment)


if __name__ == '__main__':
    main()
