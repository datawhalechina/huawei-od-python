#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 077_find-co-occurrence-number
@time:  23/8/2023 下午 8:25
@project:  huawei-od-python 
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
