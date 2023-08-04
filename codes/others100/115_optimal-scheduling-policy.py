#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 115_optimal-scheduling-policy.py
@time: 2023-07-31 15:30:29
@project: huawei-od-python
@desc: 115 最优调度策略
"""
import math


def solve_method(resources):
    min_res = math.inf
    for r in resources[0]:
        # 遍历第一个用户的策略
        total_resource = r
        preIndex = resources[0].index(r)
        for i in range(1, len(resources)):
            resource = resources[i]
            # 从除了preIndex标记以外的策略中选择对系统资源消耗最小的策略
            min_resource = min(resource[:preIndex] + resource[preIndex + 1:])
            preIndex = resource.index(min_resource)
            total_resource += min_resource
        min_res = min(min_res, total_resource)

    return min_res


if __name__ == '__main__':
    resources = [[15, 8, 17],
                 [12, 20, 9],
                 [11, 7, 5]]
    assert solve_method(resources) == 24

    resources = [[15, 12, 17],
                 [12, 3, 9],
                 [11, 7, 5]]
    assert solve_method(resources) == 23
