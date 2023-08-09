#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 081_find-city.py
@time: 2023/8/9 9:08
@project: huawei-od-python
@desc: 找城市、城市聚集度
"""
from copy import deepcopy


def solve_method(n, city_roads):
    dp = [0] * n
    for i in range(1, n + 1):
        copy_roads = deepcopy(city_roads)
        urban = []

        for x in copy_roads:
            if i in x:
                x.remove(i)

            cities = set(x)
            if len(urban) == 0:
                urban.append(cities)
            else:
                # 如果有交集，表示有道路连接到这个城市群，则为True，如果没有，则为False
                mask_city = [True if len(cities.intersection(x)) > 0 else False for x in urban]

                if not any(mask_city):
                    # 如果都没有，则添加单独城市群
                    urban.append(cities)
                else:
                    # 如果有，则直接并入已有城市群
                    index = mask_city.index(True)
                    urban[index] = urban[index].union(cities)

        # 计算聚集度dp
        dp[i - 1] = max([len(x) for x in urban])

    # 得到最小的聚集度的城市
    min_value = min(dp)
    return [i + 1 for i, x in enumerate(dp) if x == min_value]


if __name__ == '__main__':
    roads = [[1, 2],
             [2, 3],
             [3, 4],
             [4, 5]]
    assert solve_method(5, roads) == [3]

    roads = [[1, 2],
             [2, 3],
             [2, 5],
             [3, 4],
             [3, 6]]
    assert solve_method(6, roads) == [2, 3]
