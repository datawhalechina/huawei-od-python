#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 049_static-scanning-optimal-cost.py
@time: 2023/8/3 17:12
@project: huawei-od-python
@desc: 049 静态扫描最优成本
"""
from collections import defaultdict


def solve_method(m, file_ids, file_sizes):
    # count用于保存每个文件出现的次数
    count = defaultdict(int)
    # size用于保存文件的大小，即扫描成本
    size = {}

    for i in range(len(file_ids)):
        file_id = file_ids[i]
        count[file_id] += 1

        if size.get(file_id) is None:
            size[file_id] = file_sizes[i]

    result = 0
    for file_id in count.keys():
        # 每次都重新扫描的成本
        rescan_amount = count[file_id] * size[file_id]
        # 扫描一次+缓存的成本
        cached_amount = size[file_id] + m
        result += min(rescan_amount, cached_amount)
    return result


if __name__ == '__main__':
    file_ids = [1, 2, 2, 1, 2, 3, 4]
    file_sizes = [1, 1, 1, 1, 1, 1, 1]
    assert solve_method(5, file_ids, file_sizes) == 7

    file_ids = [2, 2, 2, 2, 2, 5, 2, 2, 2]
    file_sizes = [3, 3, 3, 3, 3, 1, 3, 3, 3]
    assert solve_method(5, file_ids, file_sizes) == 9
