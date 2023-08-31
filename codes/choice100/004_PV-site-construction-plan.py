#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 004_PV-site-construction-plan.py
@time: 2023/7/12 11:06
@project: huawei-od-python
@desc: 004 光伏场地建设规划
"""


def solve_method(row, col, width, power, region):
    result = 0
    # 贪心算法
    for i in range(row - width + 1):
        for j in range(col - width + 1):
            # 统计场地的所有发电量总和
            total_power = sum(
                region[m][n]
                for m in range(i, i + width)
                for n in range(j, j + width)
            )
            # 判断是否满足最低发电量
            if total_power >= power:
                result += 1

    return result


if __name__ == '__main__':
    row, col, width, power = 2, 5, 2, 6
    region = [[1, 3, 4, 5, 8],
              [2, 3, 6, 7, 1]]
    assert solve_method(row, col, width, power, region) == 4

    row, col, width, power = 2, 5, 1, 6
    region = [[1, 3, 4, 5, 8],
              [2, 3, 6, 7, 1]]
    assert solve_method(row, col, width, power, region) == 3

    row, col, width, power = 2, 5, 1, 0
    region = [[1, 3, 4, 5, 8],
              [2, 3, 6, 7, 1]]
    assert solve_method(row, col, width, power, region) == 10
