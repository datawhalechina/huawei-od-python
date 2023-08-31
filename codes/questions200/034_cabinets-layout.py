#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 034_cabinets-layout.py
@time: 2023/8/21 17:22
@project: huawei-od-python
@desc: 034 机房布局
"""


def solve_method(cabinets):
    stack = []
    # 去除重复的电箱时 - 需考虑若当前电箱是其他机柜所依赖的电箱，此时不能去除
    fixed = False
    for i in range(len(cabinets)):
        if cabinets[i] == 'M':
            is_left_invalid = i - 1 < 0 or cabinets[i - 1] == 'M'
            is_right_invalid = i + 1 == len(cabinets) or cabinets[i + 1] == 'M'
            # 若左右都没有空间放置电箱，则返回-1
            if is_left_invalid and is_right_invalid:
                return -1
            area = [max(0, i - 1), min(len(cabinets) - 1, i + 1)]
            # 去除重复放置的电箱
            if stack and not fixed:
                if stack[-1][1] == area[0]:
                    stack.pop()
                    fixed = True
            else:
                fixed = False
            stack.append(area)
    return len(stack)


if __name__ == "__main__":
    # cabinets = input().strip()
    # print(solve_method(cabinets))

    assert solve_method("MIIM") == 2
    assert solve_method("MIM") == 1
    assert solve_method("M") == -1
    assert solve_method("MMM") == -1
    assert solve_method("I") == 0
    assert solve_method("MIMIMIM") == 2
