#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 231_interval-connector.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 231 区间连接器
"""
import re

def solve_method(regions, linkers):
    # 将区间按照左端点升序排列
    regions.sort(key = lambda x: (x[0], x[1]))

    region = None
    i = 0
    # 合并重叠和相邻的区间
    while i < len(regions):
        next = regions[i]
        if region is None:
            region = next
        elif region[1] >= next[0]:
            if region[1] < next[1]:
                region[1] = next[1]
            regions.pop(i)
        else:
            region = next 
            i += 1

    gaps = [0]
    region = None
    # 计算合并后，区间之间的距离
    for i in range(len(regions)):
        next = regions[i]
        if region is not None:
            gap = next[0] - region[1]
            gaps.append(gap)
        region = next

    # 将距离和连接器长度 按照升序排列
    gaps.sort()
    linkers.sort()
    
    i = 0
    j = 0
    # 遍历计算连接器是否足够连接距离
    while i < len(gaps) and j < len(linkers):
        if linkers[j] >= gaps[i]:
            gaps[i] = 0
            i += 1
            j += 1
        else:
            j += 1

    return sum(1 for g in gaps if g > 0) + 1

if __name__ == '__main__':
    regions = [[1,10], [15, 20], [18, 30], [33, 40]]
    linkers = [5, 4, 3, 2]
    assert solve_method(regions, linkers) == 1

    regions = [[1,2], [3, 5], [7, 10], [15, 20], [30, 100]]
    linkers = [5, 4, 3, 2, 1]
    assert solve_method(regions, linkers) == 2
    