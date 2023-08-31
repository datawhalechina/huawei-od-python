#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 013_interval-connector.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 013 区间连接器
"""


def solve_method(regions, linkers):
    # 将区间按照左端点从小到大排列
    regions.sort(key=lambda x: (x[0], x[1]))

    prev_region = None
    i = 0
    # 合并重叠和相邻的区间
    while i < len(regions):
        cur_region = regions[i]
        if prev_region is None:
            prev_region = cur_region
        elif prev_region[1] >= cur_region[0]:
            # 如果重叠
            if prev_region[1] < cur_region[1]:
                # 合并区域
                prev_region[1] = cur_region[1]
            regions.pop(i)
        else:
            prev_region = cur_region
            i += 1

    distances = [0]
    prev_region = None
    # 计算合并后，区间之间的距离
    for i in range(len(regions)):
        cur_region = regions[i]
        if prev_region is not None:
            gap = cur_region[0] - prev_region[1]
            distances.append(gap)
        prev_region = cur_region

    # 将距离和连接器长度按照从小到大排列
    distances.sort()
    linkers.sort()

    i = 0
    j = 0
    # 遍历计算连接器是否足够连接距离
    while i < len(distances) and j < len(linkers):
        if linkers[j] >= distances[i]:
            distances[i] = 0
            i += 1
            j += 1
        else:
            j += 1

    return len(list(filter(lambda x: x > 0, distances))) + 1


if __name__ == '__main__':
    regions = [[1, 10], [15, 20], [18, 30], [33, 40]]
    linkers = [5, 4, 3, 2]
    assert solve_method(regions, linkers) == 1

    regions = [[1, 2], [3, 5], [7, 10], [15, 20], [30, 100]]
    linkers = [5, 4, 3, 2, 1]
    assert solve_method(regions, linkers) == 2
