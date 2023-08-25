#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 077_find-co-occurrence-number
@time:  2023/8/23 20:25
@project:  huawei-od-python
@desc: 077 找出两个整数数组中同时出现的整数
"""
from collections import Counter


def solve_method(nums1, nums2):
    c1 = dict(Counter(nums1))
    c2 = dict(Counter(nums2))
    common = set(c1.keys()) & set(c2.keys())
    record = dict()
    for number in common:
        freq = min(c1[number], c2[number])
        if freq not in record:
            record[freq] = [number]
        else:
            record[freq].append(number)
    items = sorted(record.items())
    items = [[item[0], sorted(item[1])] for item in items]
    output = []
    for item in items:
        output.append(f'{item[0]}:' + ','.join(map(str, item[1])))

    return '\n'.join(output)


if __name__ == '__main__':
    nums1 = list(map(int, input().strip().split(',')))
    nums2 = list(map(int, input().strip().split(',')))
    res = solve_method(nums1, nums2)
    print(res)
